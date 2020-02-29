from django.core.cache import cache 
from django.db.models import F, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from apps.account.models import UserProfile
from apps.fans.models import Fans
from apps.fans.serializers import FansSerializer, ListFansSerializer
from apps.util.page import StandardPagination
from apps.util.permission import StandardPermission

class FansViewset(mixins.CreateModelMixin,mixins.ListModelMixin, \
   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (StandardPermission, )
    pagination_class = StandardPagination
    queryset = Fans.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ('follower', 'followee')

    def get_serializer_class(self):
        if self.action in ('list', ):
            return ListFansSerializer
        else:
            return FansSerializer

    def create(self, request, *args, **kwargs):
        follower = self.request.data.get('follower', None)
        followee = self.request.data.get('followee', None)

        if not(follower or followee):
            return Response({
                'msg':'参数缺失'
            }, status=400)
        if follower==followee:
            return Response({
                'msg':'不要关注自己'
            }, status=400)

        follower = UserProfile.objects.filter(id=follower).first()
        if not follower:
            return Response({
                'msg': '无follower用户'
            }, status=400)

        followee = UserProfile.objects.filter(id=followee).first()
        if not followee:
            return Response({
                'msg': '无followee用户'
            }, status=400)
        
        fan = Fans.objects.create(
            follower=follower,
            followee=followee
        )
        return Response({
            'msg':'关注成功',
            'data': fan.id
        }, status=200)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.check_id_authuser(self.request.user):
            return Response({
                'msg':'错误操作'
            }, status=400)
        instance.destroy()

        return Response({
            'msg': '评论删除成功'
        }, status=200)




