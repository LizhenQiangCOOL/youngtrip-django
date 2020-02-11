from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

#　设置默认　celery命令行程序环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youngtrip.settings')

app = Celery('youngtrip', backend='redis://:w9jTwtNi1wm4Q3VPUfBecPWd@redis:6379/0', broker='amqp://root:w9jTwtNi1wm4Q3VPUfBecPWd@rabbit:5672//')

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