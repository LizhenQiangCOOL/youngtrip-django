from django.contrib import admin
from apps.card.models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic', 'content', 'date', 'location', 'createtime', 'updatetime', 'trip', 'userprofile')
    list_editable = ( 'pic', 'content', 'date', 'location', 'trip', 'userprofile')
    search_fields = ('content', 'location')
    list_filter = ('trip', 'userprofile', 'date')

