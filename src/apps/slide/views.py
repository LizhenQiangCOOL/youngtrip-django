from django.core.cache import cache 
from django.db.models import F, Q
from django.core import serializers
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from apps.slide.models import Slide
from apps.slide.serializers import SlideSerializer
from apps.util.permission import StandardPermission

class SlideViewSet(viewsets.ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (StandardPermission, )
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)