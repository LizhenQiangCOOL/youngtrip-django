from django.db import models

from apps.account.models import UserProfile

class Fans(models.Model):
    """
     follower(id) -> followee(id)
     关注者id -> 被关注人id
    """    
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userprofile_followee', verbose_name='关联Userprofile追随')
    followee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='userprofile_follower', verbose_name='关联Userprofile粉丝')
   
    def __str__(self):
        return '<Fans:{}>'.format(self.id)

    def check_id_authuser(self, user):
        return (user.id == self.follower.user.id) and (user.id != self.followee.user.id)
    
    class Meta:
        verbose_name = verbose_name_plural = "粉丝"
        unique_together = (('follower','followee'),)