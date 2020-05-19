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
from apps.trip.models import Trip
from apps.trip.serializers import TripSerializer, ReTripSerializer
from apps.util.page import StandardPagination
from apps.util.permission import StandardPermission


class TripViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (StandardPermission, )
    # queryset = Trip.objects.all()
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('userprofile', )
    search_fields = ('title',)

    def get_queryset(self):
        if self.action in ('retrieve', 'list'):
            return Trip.objects.all().filter(status='1')
        else:
            return Trip.objects.all()
    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ReTripSerializer
        else:
            return TripSerializer
    
    def create(self, request, *args, **kwargs):
        userprofile = self.request.user.user_userprofile
        title = self.request.data.get('title', None)
        pic = self.request.data.get('pic', None)
        firstday = self.request.data.get('firstday', None)
        location = self.request.data.get('location', None)

        if not (userprofile or title or pic or firstday or location):
            return Response({
                'msg':'缺参数'
            }, status=400)
        
        trip = Trip.objects.create(
            userprofile=userprofile,
            title=title,
            pic=pic,
            firstday=firstday,
            location=location,
        )
        return Response({
            'msg':'游记创建成功',
            'data':{'id':trip.id}
        }, status=200)
    
    def update(self, request, *args, **kwargs):
        user = self.request.user
        title = self.request.data.get('title', None)
        pic = self.request.data.get('pic', None)
        status = self.request.data.get('status', None)
        firstday = self.request.data.get('firstday', None)
        location = self.request.data.get('location', None)

        instance = self.get_object()

        if user.id != instance.userprofile.user.id:
            return Response({
                'msg':'错误操作',
            }, status=400)

        if title:
            instance.title = title
        if pic:
            instance.pic = pic
        if status:
            instance.status = status
        if firstday:
            instance.firstday = firstday
        if location:
            instance.location = location
        
        instance.save()
        
        return Response({
            'msg':'游记修改成功'
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
            'msg':'游记删除成功'
        }, status=200)
