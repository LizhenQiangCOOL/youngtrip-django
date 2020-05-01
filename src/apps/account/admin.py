from django.contrib import admin
from apps.account.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar', 'sex', 'sign', 'user')
    list_editable = ('avatar', 'sex', 'sign', 'user')
    search_fields = ()
    list_filter = ('sex', )


