from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.slide.views import SlideViewSet

router = DefaultRouter()
router.register('slide', SlideViewSet, 'slide')

urlpatterns = [
    path('', include(router.urls)),  
]