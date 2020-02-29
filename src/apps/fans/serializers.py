from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.account.serializers import ReCardUserSerializer
from apps.fans.models import Fans

class FansSerializer(serializers.ModelSerializer):
    follower = serializers.IntegerField()
    followee = serializers.IntegerField()
    class Meta:
        model = Fans
        fields = ('id', 'follower', 'followee')
        validators = [UniqueTogetherValidator(queryset=Fans.objects.all(),\
             fields=('follower', 'followee'), message='你已follow')]

class ListFansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fans
        fields = '__all__'

class ListFollowerSerializer(serializers.ModelSerializer):
    """
    获取谁关注你
    """    
    follower = serializers.SerializerMethodField()

    def get_fan(self, obj):
        return ReCardUserSerializer(obj.follower).data
        
    class Meta:
        model = Fans
        fields = ('id', 'follower')

class ListFolloweeSerializer(serializers.ModelSerializer):
    """
    获取你关注谁
    """
    followee = serializers.SerializerMethodField()
    
    def get_follow(self, obj):
        return ReCardUserSerializer(obj.followee).data
    
    class Meta:
        model = Fans
        fields = ('id', 'followee')
