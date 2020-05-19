from django.contrib import admin
from apps.trip.models import Trip

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pic', 'firstday', 'location', 'status', 'likecount', 'commentcount', 'createtime', 'updatetime', 'userprofile')
    list_editable = ('title', 'pic', 'firstday', 'location', 'status', 'userprofile')
    search_fields = ('title', 'userprofile')
    list_filter = ('userprofile', )