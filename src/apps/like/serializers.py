from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.account.serializers import ReCardUserSerializer
from apps.like.models import Like

class LikeSerializer(serializers.ModelSerializer):
    card = serializers.IntegerField()
    userprofile = serializers.IntegerField()
    class Meta:
        model = Like
        fields = ('id', 'card', 'userprofile')
        validators = [UniqueTogetherValidator(queryset=Like.objects.all(),\
             fields=('card', 'userprofile'), message='你已like')]


class ListLikeSerializer(serializers.ModelSerializer):
    userprofile = serializers.SerializerMethodField()

    def get_userprofile(self, obj):
        return ReCardUserSerializer(obj.userprofile).data
        
    class Meta:
        model = Like
        fields = ('id', 'userprofile')





    
