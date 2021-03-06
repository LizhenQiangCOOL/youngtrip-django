from rest_framework import serializers

from apps.account.serializers import ReCardUserSerializer
from apps.card.models import Card
from apps.comment.serializers import ListCommentSerializer
from apps.like.serializers import ListLikeSerializer

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ReCardSerializer(serializers.ModelSerializer):
    userprofile = serializers.SerializerMethodField()
    likeUsers = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    dateD = serializers.SerializerMethodField()

    def get_userprofile(self, obj):
        return ReCardUserSerializer(obj.userprofile).data
    
    def get_likeUsers(self, obj):
        return ListLikeSerializer(obj.card_like.all(), many=True).data
    
    def get_comments(self, obj):
        return ListCommentSerializer(obj.card_comment.all(), many=True).data
    
    def get_dateD(self, obj):
        return obj.date.date().strftime('%Y-%m-%d')
    class Meta:
        model = Card
        fields = ('userprofile', 'id', 'pic', 'content', 'location', 'date', 'dateD', 'likeUsers', 'comments')