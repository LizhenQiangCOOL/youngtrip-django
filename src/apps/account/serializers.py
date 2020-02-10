from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.account.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=10, required=True, help_text="用户名")
    password = serializers.CharField(min_length=6, max_length=16, required=True, style={
        'input_type': 'password'
    }, help_text='密码')

    class Meta:
        model = User
        fields = ('username', 'password')
        
class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=10, required=True, help_text="用户名")
    password = serializers.CharField(min_length=6, max_length=16, required=True, style={
        'input_type': 'password'
    }, help_text='密码')
    code = serializers.CharField(max_length=7, required=True, help_text='验证码')
    avator = serializers.CharField(max_length=100, required=True, help_text='头像')
    class Meta:
        model = User
        fields = ('username', 'email', 'code', 'password', 'avator')


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3, max_length=10, help_text="用户名")
    password = serializers.CharField(min_length=6, max_length=16, style={
        'input_type': 'password'
    }, help_text='密码')
    email = serializers.EmailField()
    class Meta:
        model = UserProfile

        fields = ('username', 'password', 'email', 'avatar', 'sex', 'sign')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'avatar', 'sex', 'sign')


class ReCardUserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username if obj.user.username else ''

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'avatar')
    