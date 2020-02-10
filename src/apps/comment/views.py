from django.core.cache import cache 
from django.db.models import F, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.account.models import UserProfile
from apps.card.models import Card
from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer, ListCommentSerializer
from apps.util.page import StandardPagination
from apps.util.permission import StandardPermission


class CommentViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,\
    mixins.DestroyModelMixin, viewsets.GenericViewSet):

    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (StandardPermission, )
    pagination_class = StandardPagination
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return ListCommentSerializer
        else:
            return CommentSerializer

    def create(self, request, *args, **kwargs):
        card = self.request.data.get('card', None)
        userprofile = self.request.data.get('userprofile', None)
        content = self.request.data.get('content', None)
        
        if not(card or userprofile or content):
            return Response({
                'msg':'参数缺失'
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
        
       
        comment = Comment.objects.create(
            card=card,
            userprofile=userprofile,
            content=content,
        )
        serializer = self.get_serializer(comment)
        return Response({
            'msg':'评论成功',
            'data': serializer.data
        }, status=200)
    
    def update(self, request, *args, **kwargs):
        content = self.request.data.get('content', None)
        instance = self.get_object()

        if content:
            instance.content = content
        instance.save()
        return Response({
            'msg': '评论修改成功'
        }, status=200)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.destroy()

        return Response({
            'msg': '评论删除成功'
        }, status=200)