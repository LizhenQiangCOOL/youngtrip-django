import os
import datetime
from django.db import models

from apps.account.models import UserProfile

class Trip(models.Model):
    Status_TYPE = (
        ('0', '未激活'),
        ('1', '已激活')
    )
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="userprofile_trip", verbose_name='关联Userprofile')
    title = models.CharField(max_length=80, null=True, blank=True, help_text='标题', verbose_name='标题')
    pic = models.CharField(max_length=100, null=True, blank=True, help_text='封面图', verbose_name='封面图')
    firstday = models.DateField(null=True, blank=True,  help_text='游记第一天时间', verbose_name='游记第一天时间')
    location = models.CharField(max_length=50, null=True, blank=True, help_text='主要地点', verbose_name='主要地点')

    status = models.CharField(max_length=3, choices=Status_TYPE, null=True, blank=True, default=Status_TYPE[0][0], help_text='状态', verbose_name='状态')
    likecount = models.IntegerField(null=True, blank=True, default=0, help_text='喜欢数目', verbose_name='喜欢数目')
    commentcount = models.IntegerField(null=True, blank=True, default=0,  help_text='评论数目', verbose_name='评论数目')
    
    createtime = models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')
    updatetime = models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')

    def __str__(self):
        return '<Trip:{}>'.format(self.id)
    
    class Meta:
        verbose_name = verbose_name_plural = "游记"
        ordering = ['-createtime']