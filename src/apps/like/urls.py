from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.like.views import LikeViewset

router = DefaultRouter()
router.register('like', LikeViewset, 'like')

urlpatterns = [
    path('', include(router.urls)),  
]