import os
import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


def slide_pic_path(instance, filename):
    """卡片版图上传路径"""
    extension = os.path.splitext(filename)[1]
    now = datetime.datetime.now()
    filename = 'slide/' + now.strftime('%y%m%d_%H%M%S')+ extension
    return filename

class Slide(models.Model):
    pic = models.ImageField(upload_to=slide_pic_path,null=False, blank=False,default='', help_text='图片', verbose_name='图片')
    content = RichTextUploadingField(null=True, blank=True, help_text='轮播图内容', verbose_name='轮播图内容')
    remark = models.CharField(max_length=50, null=True, blank=True, help_text='备注', verbose_name='备注')
    createtime = models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')
    updatetime = models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')

    def __str__(self):
        return '<Slide:{}>'.format(self.id)

    class Meta:
        db_table = "slide"
        verbose_name = verbose_name_plural = "轮播图"
        ordering = ['-createtime']