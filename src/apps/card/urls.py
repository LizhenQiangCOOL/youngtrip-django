from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.card.views import CardViewSet, LikeCardViewSet

router = DefaultRouter()
router.register('card', CardViewSet, 'card')
router.register('likecard', LikeCardViewSet, 'likecard')


urlpatterns = [
    path('', include(router.urls)),  
    # path('likecard', LikeCardViewSet.as_view({'get':'list'}))
]