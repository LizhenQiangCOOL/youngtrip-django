from django.contrib import admin
from apps.card.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pic', 'content', 'date', 'location', 'createtime', 'updatetime', 'userprofile')
    list_editable = ('title', 'pic', 'content', 'date', 'location')
    search_fields = ('title', 'content', 'location')
    list_filter = ('userprofile', 'date')
