from rest_framework import serializers

from apps.account.serializers import ReCardUserSerializer
from apps.account.serializers import ReCardSerializer
from apps.card.models import Card
from apps.trip.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class ReTripSerializer(serializers.ModelSerializer):
    userprofile = serializers.SerializerMethodField()
    cards = serializers.SerializerMethodField()

    def get_userprofile(self, obj):
        return ReCardUserSerializer(obj.userprofile).data
    
    def get_cards(self, obj):
        return ReCardSerializer(obj.trip_card.all().order_by('date'), many=True).data
     
    class Meta:
        model = Trip
        fields = ('userprofile', 'id', 'title', 'pic', 'likecount', 'commentcount', 'cards')

