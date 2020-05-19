from django.contrib import admin
from apps.file.models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'createtime')
    list_editable = ('file', 'type')
    list_filter = ('type', )