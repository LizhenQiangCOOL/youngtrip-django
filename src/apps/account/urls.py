from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.account.views import LoginViewSet, RegisterViewSet, UserProfileViewSet, EmailEnsureViewSet, \
    EmailCodeSendViewSet

router = DefaultRouter()
router.register('login', LoginViewSet, 'login')
router.register('register', RegisterViewSet, 'register')
router.register('user', UserProfileViewSet, 'user')



urlpatterns = [
    path('', include(router.urls)),  
    path('emailcode', EmailEnsureViewSet.as_view({'post':'create'})),
    path('emailcodesend', EmailCodeSendViewSet.as_view({'post':'create'})),
]