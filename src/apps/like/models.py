from django.db import models

from apps.account.models import UserProfile
from apps.card.models import Card

class Like(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card_like', verbose_name='关联Userprofile')
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userprofile_like', verbose_name='关联游记卡片')
    
    def __str__(self):
        return '<Like:{}>'.format(self.id)

    def check_id_authuser(self, user):
        return user.id == self.userprofile.user.id
    
    class Meta:
        db_table = "like"
        verbose_name = verbose_name_plural = "喜欢"
        unique_together = (('card','userprofile'),)