from __future__ import absolute_import, unicode_literals

import os
import requests
from .settings import BASE_DIR
from celery import Celery
from celery.schedules import crontab

#　设置默认　celery命令行程序环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youngtrip.settings')

BACKEND_URL = 'redis://:w9jTwtNi1wm4Q3VPUfBecPWd@redis:6379/0'
BROKER_URL = 'amqp://root:w9jTwtNi1wm4Q3VPUfBecPWd@rabbit:5672//'

app = Celery('youngtrip', backend=BACKEND_URL, broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Shanghai',
    enable_utc=True,
)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# 测试
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))




# 定时任务 Beta
# 时间表
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'youngtrip.celery.download_headbg',
        'schedule': crontab(minute='*/15'),
        'args': ('https://picsum.photos/1920/1080?random',)
    },
}



@app.task
def download_headbg(url):
    try:
        r = requests.get(url, stream=True)
        if(r.status_code == 200):
            open(os.path.join(BASE_DIR, 'media', 'img', 'headbg.png'), 'wb').write(r.content)
            return 'headbg下载成功'
    except Exception as identifier:
        return 'headbg下载失败'