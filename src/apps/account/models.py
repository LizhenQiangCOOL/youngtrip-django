from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    SEX_TYPE = (
        ('0', '未选择'),
        ('male', '男'),
        ('female', '女')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_userprofile', verbose_name='关联User')
    avatar = models.CharField(max_length=100, null=True, blank=True, help_text='用户头像', verbose_name='用户头像')
    sex = models.CharField(max_length=10,null=True, blank=True, choices=SEX_TYPE, default=SEX_TYPE[0][0], help_text='性别', verbose_name='性别')
    sign = models.CharField(max_length=100, null=True, blank=True, default='', help_text='个性签名', verbose_name='个性签名')

    def __str__(self):
        return '<UserProfile:{}-{}>'.format(self.id, self.user)
    class Meta:
        db_table = "userprofile"
        verbose_name = verbose_name_plural = "用户profile"
