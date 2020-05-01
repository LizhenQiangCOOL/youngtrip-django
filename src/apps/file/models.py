import os
import datetime
from django.db import models

def card_pic_path(instance, filename):
    """卡片版图上传路径"""
    extension = os.path.splitext(filename)[1]
    now = datetime.datetime.now()
    filename = 'card/' + now.strftime('%y%m%d_%H%M%S')+ extension
    return filename

class File(models.Model):
    File_TYPE = (
        ('', '未知'),
        ('img', '图片'),
        ('video', '视频')
    )
    file = models.FileField(upload_to=card_pic_path,null=True, blank=True, help_text='上传的文件', verbose_name='上传的文件')
    type = models.CharField(max_length=10, choices=File_TYPE, null=True, blank=True, default=File_TYPE[0][0], help_text='文件类型', verbose_name='文件类型')
    createtime = models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')

    def __str__(self):
        return '<File:{}>'.format(self.id)
    
    class Meta:
        db_table = "file"
        verbose_name = verbose_name_plural = "文件"