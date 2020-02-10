from django.contrib import admin
from apps.like.models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'userprofile')
    list_editable = ('card', 'userprofile')
    list_filter = ('card', 'userprofile')