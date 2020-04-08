import os
import datetime
from django.db import models

from apps.account.models import UserProfile
from apps.trip.models import Trip

def card_pic_path(instance, filename):
    """卡片版图上传路径"""
    #拿后缀
    extension = os.path.splitext(filename)[1]
    now = datetime.datetime.now()
    filename = 'card/image/' + now.strftime('%y%m%d_%H%M%S')+ extension
    return filename

class Card(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userprofle_card', verbose_name='关联Userprofile')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="trip_card",  verbose_name='关联Trip')
    # title = models.CharField(max_length=80,default='test', null=True, blank=True, help_text='标题', verbose_name='标题')
    pic = models.CharField(max_length=100, null=True, blank=True, help_text='图片', verbose_name='图片')
    content = models.CharField(max_length=400, null=True, blank=True, help_text='内容', verbose_name='内容')
    date = models.DateTimeField(null=True, blank=True, help_text='游记卡片时间', verbose_name='游记卡片时间')
    location = models.CharField(max_length=50, null=True, blank=True, help_text='地点', verbose_name='地点')
    createtime = models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')
    updatetime = models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')

    def __str__(self):
        return '<Card:{}>'.format(self.id)

    class Meta:
        verbose_name = verbose_name_plural = "游记卡片"
        ordering = ['-createtime']
        
    
    
