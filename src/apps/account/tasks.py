
from __future__ import absolute_import, unicode_literals
import time
from django.core.mail import send_mail 
from django.conf import settings
from celery import shared_task


@shared_task
def add(x, y):
    print(x+y)
    return x + y

@shared_task
def sendemail(receiver,contentletter=''):
    subject = '青年游记'
    message='验证码'
    sender = settings.EMAIL_FROM 
    receiver = (receiver,)
    html_message = "<h2>您这次的验证码是：</h2><h4>"+contentletter+"</h4>"
    send_mail(subject, message, sender, receiver, html_message=html_message)
    time.sleep(1)

