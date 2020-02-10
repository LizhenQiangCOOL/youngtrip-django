import random

from django.core.cache import cache 
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from apps.account.models import UserProfile
from apps.account.serializers import LoginSerializer, CreateUserSerializer, UpdateUserProfileSerializer, \
    UserProfileSerializer
from apps.account.tasks import sendemail
from apps.util.page import StandardPagination
from apps.util.permission import StandardPermission


def _jwt_to_encode(obj):
    jwt_payload = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload(obj)
    return jwt_encode(payload)

def letterNumber(length=6):
    return ''.join(random.choice('123456789') for i in range(length))

class LoginViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:登陆 
        返回JWT  之后放在HTTP header中 Authorization: 'JWT '+token 
        测试账号：admin   youngtrip
    """
    queryset = UserProfile.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        username = self.request.data.get('username', None)
        password = self.request.data.get('password', None)

        userprofile = self.queryset.filter(user__username=username).first()

        if not userprofile:
            return Response({
                'msg':'没有该用户'
            }, status=404)
        if not userprofile.user.check_password(password):
                return Response({
                    'msg':'密码错误'
                }, status=400)
        
        jwt_token = _jwt_to_encode(userprofile.user)
        serializer = UserProfileSerializer(userprofile)
        return Response({
            'data':{
                'token': jwt_token,
                'userinfo': serializer.data
            }
        }, status=200)

class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:注册用户
    """    
    queryset = UserProfile.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        username = self.request.data.get('username', None)
        password = self.request.data.get('password', None)
        email = self.request.data.get('email', None)
        code = self.request.data.get('code', None)
        avatar = self.request.data.get('avatar', None)

        if not(username and password and email and avatar):
            return Response({
                'msg':'字段填写不全'
                }, status=400)               
        if User.objects.filter(username=username).exists():
            return Response({
                'msg':'该用户名已经存在'
            }, status=400)
        if User.objects.filter(email=email).exists():
            return Response({
                'msg':'该邮箱已被占用'
            }, status=400)
        rediscode = cache.get(email)
        if rediscode is None:
            return Response({
                'msg':'验证码过期'
            }, status=400)
        if rediscode != code:
            return Response({
                'msg':'验证码不正确'
            }, status=400)
        user = User.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        userprofile = UserProfile.objects.create(
            avatar=avatar,
            user=user,
        )

        jwt_token = _jwt_to_encode(user)
        serializer = UserProfileSerializer(userprofile)
        return Response({
            'msg':'注册成功',
            'data':{
                'token': jwt_token,
                'userinfo': serializer.data
            }
        }, status=200)


class UserProfileViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (StandardPermission,)
    queryset = UserProfile.objects.all()
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action == 'update':
            return UpdateUserProfileSerializer
        else:
            return UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserProfileSerializer(instance)
        return Response({
            'data':{
                'userinfo': serializer.data
            }
        }, status=200)

    def update(self, request, *args, **kwargs):
        username = self.request.data.get('username', None)
        password = self.request.data.get('password', None)
        email = self.request.data.get('email', None)
        avatar = self.request.data.get('avatar', None)
        sex = self.request.data.get('sex', None)
        sign = self.request.data.get('sign', None)

        instance = self.get_object()

        if username and User.objects.filter(username=username).exists():
            return Response({
                'msg':'该用户名已经存在'
            }, status=400)
        if email and User.objects.filter(email=email).exists():
            return Response({
                'msg':'该邮箱已被占用'
            }, status=400)

        user = instance.user
        if username:
            user.username = username
        if password:
            user.set_password(password)
        if email:
            user.email = email
        if avatar:
            instance.avatar = avatar
        if sex:
            instance.sex = sex
        if sign:
            instance.sign = sign
        user.save()
        instance.save()

        serializer = UserProfileSerializer(instance)
        return Response({
            'msg':'修改成功',
            'data':{
                'userinfo': serializer.data
            }
        }, status=200)


class EmailCodeSendViewSet(viewsets.ViewSet):
    """
    　邮箱验证码发送, 参数：email='xxx@xx.com'
    """    
    def create(self, request, *args, **kwargs):
        email = self.request.data.get('email', None)
        if not (email):
            return Response({
                'msg':'缺邮箱地址'
            }, status=400)
        if cache.get(email+'_lock'):
            return Response({
                'msg':'邮件发送太频繁了'
            }, status=400)
        code = letterNumber()
        sendemail.delay(email, code)
        cache.set(email, code, timeout=10*60) 
        cache.set(email+'_lock', True, timeout=30)
        return Response({
            'msg':'验证码发送成功'
        }, status=200)

class EmailEnsureViewSet(viewsets.ViewSet):
    """
    　邮箱验证码验证, 参数：email='xxx@xx.com' code='验证码'
    """    
    def create(self, request, *args, **kwargs):
        email = self.request.data.get('email', None)
        code = self.request.data.get('code', None)

        if not (email and code):
            return Response({
                'msg':'缺邮箱地址'
            }, status=400)
        rediscode = cache.get(email)
        if rediscode is None:
            return Response({
                'msg':'验证码过期'
            }, status=400)
        if rediscode != code:
            return Response({
                'msg':'验证码不正确'
            }, status=400)
        if not User.objects.filter(email=email).exists():
            return Response({
                'msg':'用户不存在'
            }, status=400)
        
        userprofile =  UserProfile.objects.all().filter(user__email=email).first()
        jwt_token = _jwt_to_encode(userprofile.user)
        serializer = UserProfileSerializer(userprofile)
        return Response({
            'data':{
                'token': jwt_token,
                'userinfo': serializer.data
            }
        }, status=200)
