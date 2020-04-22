from django.contrib import admin
from apps.slide.models import Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic', 'content', 'remark', 'createtime', 'updatetime')
    list_editable = ( 'pic', 'content', 'remark')
    search_fields = ('content', )
    list_filter = ('createtime',)
