from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.comment.views import CommentViewset

router = DefaultRouter()
router.register('comment', CommentViewset, 'comment')

urlpatterns = [
    path('', include(router.urls)),  
]