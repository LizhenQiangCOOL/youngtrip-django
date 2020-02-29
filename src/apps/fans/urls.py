from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.fans.views import FansViewset

router = DefaultRouter()
router.register('fans', FansViewset, 'fans')

urlpatterns = [
    path('', include(router.urls)),  
]