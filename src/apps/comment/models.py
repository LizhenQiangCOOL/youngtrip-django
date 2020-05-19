from django.db import models

from apps.account.models import UserProfile
from apps.card.models import Card

class Comment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card_comment', verbose_name='关联游记卡片')
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userprofile_comment', verbose_name='关联用户profile')
    content = models.CharField(max_length=100, null=True, blank=True, help_text='评论内容', verbose_name='评论内容')
    date = models.DateTimeField(auto_now=True, verbose_name='评论时间')

    def __str__(self):
        return '<Comment:{}>:'.format(self.id)
    
    class Meta:
        db_table = "comment"
        verbose_name = verbose_name_plural = '评论'