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

