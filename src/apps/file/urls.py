from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.file.views import FileViewSet

router = DefaultRouter()
router.register('file', FileViewSet, 'files')

urlpatterns = [
    path('', include(router.urls)),  
]