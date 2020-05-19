from django.core.cache import cache 
from django.db.models import F, Q
from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend


from apps.account.models import UserProfile
from apps.card.models import Card
from apps.like.models import Like
from apps.trip.models import Trip
from apps.card.serializers import CardSerializer, ReCardSerializer
from apps.util.page import StandardPagination
from apps.util.permission import StandardPermission


class CardViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (StandardPermission, )
    queryset = Card.objects.all()
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('userprofile', 'location')
    search_fields = ('content', 'location')


    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ReCardSerializer
        else:
            return CardSerializer

    def create(self, request, *args, **kwargs):
        userprofile = self.request.user.user_userprofile
        # title = self.request.data.get('title', None)
        trip = int(self.request.data.get('trip', None))
        pic = self.request.data.get('pic', None)
        content = self.request.data.get('content', None)
        date = self.request.data.get('date', None)
        location = self.request.data.get('location', None)

        if not (userprofile or trip  or pic or content or date or location):
            return Response({
                'msg':'缺参数'
            }, status=400)
        
        trip = Trip.objects.filter(id=trip).first()
        if trip == None:
            return Response({
                'msg': '错误操作'
            }, status=400)

        card = Card.objects.create(
            userprofile=userprofile,
            trip=trip,
            pic=pic,
            content=content,
            date=date,
            location=location,
        )
        return Response({
            'msg':'游记卡片创建成功',
            'data':{'id':card.id, 'pic':card.pic, 'content':card.content},
        }, status=200)
    
    def update(self, request, *args, **kwargs):
        user = self.request.user.user_userprofile
        # title = self.request.data.get('title', None)
        pic = self.request.data.get('pic', None)
        content = self.request.data.get('content', None)
        date = self.request.data.get('date', None)
        location = self.request.data.get('location', None)
        
        instance = self.get_object()

        if user.id != instance.userprofile.user.id:
            return Response({
                'msg':'错误操作',
            }, status=400)

        # if title:
        #     instance.title = title
        if pic:
            instance.pic = pic
        if content:
            instance.content = content
        if date:
            instance.date = date
        if location:
            instance.location = location
        instance.save()

        return Response({
            'msg':'游记卡片修改成功',
        }, status=200)    

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        instance = self.get_object()
        if user.id != instance.userprofile.user.id:
            return Response({
                'msg':'错误操作',
            }, status=400)

        instance.delete()
        return Response({
            'msg':'游记卡片删除成功'
        }, status=200)



class LikeCardViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    queryset = Card.objects.all()
    pagination_class = StandardPagination
    serializer_class = ReCardSerializer


    def list(self, request, *args, **kwargs):
        userprofile = self.request.query_params.get('userprofile', None)
        if not userprofile:
             return Response({
                'msg':'缺参数'
            }, status=400)
        userprofile = UserProfile.objects.filter(id=userprofile).first()
        if not userprofile:
            return Response({
                'msg':'用户不存在'
                }, status=400) 
        if self.request.user.id != userprofile.user.id:
            return Response({
                'msg':'错误操作'
                }, status=400) 

        idlist = [like.card_id for like in Like.objects.filter(userprofile=userprofile)]

        queryset = self.get_queryset().filter(id__in=idlist)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
