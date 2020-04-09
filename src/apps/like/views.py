from django.core.cache import cache
from django.db.models import F, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.account.models import UserProfile
from apps.card.models import Card
from apps.like.models import Like
from apps.like.serializers import LikeSerializer, ListLikeSerializer
from apps.util.page import StandardPagination
from apps.util.permission import StandardPermission


class LikeViewset(mixins.CreateModelMixin, mixins.ListModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):

    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (StandardPermission, )
    pagination_class = StandardPagination
    queryset = Like.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return ListLikeSerializer
        else:
            return LikeSerializer

    def create(self, request, *args, **kwargs):
        card = self.request.data.get('card', None)
        userprofile = self.request.data.get('userprofile', None)

        if not(card or userprofile):
            return Response({
                'msg': '参数缺失'
            }, status=400)

        card = Card.objects.filter(id=card).first()
        if not card:
            return Response({
                'msg': '无此游记'
            }, status=400)
        userprofile = UserProfile.objects.filter(id=userprofile).first()
        if not userprofile:
            return Response({
                'msg': '无此用户'
            }, status=400)

        if self.get_queryset().filter(Q(card=card) & Q(userprofile=userprofile)).exists():
            return Response({
                'msg': '已like'
            }, status=400)

        like = Like.objects.create(
            card=card,
            userprofile=userprofile
        )
        trip = card.trip
        trip.likecount += 1
        trip.save()

        serializer = self.get_serializer(like)
        return Response({
            'msg': 'like成功',
            'data': serializer.data
        }, status=200)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     queryset = self.filter_queryset(queryset)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response({
    #         'data':serializer.data
    #     }, status=200)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.check_id_authuser(self.request.user):
            return Response({
                'msg': '错误操作'
            }, status=400)
            
        trip = instance.card.trip
        trip.likecount -= 1
        trip.save()

        instance.delete()

        return Response({
            'msg': '评论删除成功'
        }, status=200)
