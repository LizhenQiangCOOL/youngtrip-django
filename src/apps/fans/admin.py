from django.contrib import admin
from apps.fans.models import Fans

@admin.register(Fans)
class FansAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'followee')
    list_editable = ('follower', 'followee')
    list_filter = ('follower', 'followee')