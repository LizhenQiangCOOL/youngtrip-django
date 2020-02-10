from django.contrib import admin
from apps.comment.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date', 'card', 'userprofile')
    list_editable = ('content', 'card', 'userprofile')
    search_fields = ('content', )
    list_filter = ('date', 'card', 'userprofile')

