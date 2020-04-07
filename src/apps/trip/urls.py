from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.trip.views import TripViewSet

router = DefaultRouter()
router.register('trip', TripViewSet, 'trip')

urlpatterns = [
    path('', include(router.urls)),  
]