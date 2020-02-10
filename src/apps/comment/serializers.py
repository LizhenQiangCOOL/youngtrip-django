from rest_framework import serializers

from apps.account.serializers import ReCardUserSerializer
from apps.comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    card = serializers.IntegerField()
    userprofile = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = '__all__'

class ListCommentSerializer(serializers.ModelSerializer):
    userprofile = serializers.SerializerMethodField()

    def get_userprofile(self, obj):
        return ReCardUserSerializer(obj.userprofile).data
    
    class Meta:
        model = Comment
        fields = ('id', 'userprofile', 'content', 'date')