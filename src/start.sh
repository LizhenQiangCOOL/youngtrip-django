#!/bin/bash
# 1. 守护进程执行 celery，后台运行
# 2. 收集静态文件到根目录，
# 3. 生成数据库可执行文件，
# 4. 根据数据库可执行文件来修改数据库
# 5. 用 gunicorn 启动 django 服务，后台运行
# 6. 启动flower

rm -rf *.pid&&
celery multi start w1 -A youngtrip worker -l info &&

python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&

gunicorn -D youngtrip.wsgi:application -w 2 -b 0.0.0.0:8000 -k gevent &&
#gunicorn youngtrip.wsgi:application -c gunicorn.conf
#python manage.py runserver 0.0.0.0:8000
celery  flower -A youngtrip --basic_auth=root:w9jTwtNi1wm4Q3VPUfBecPWd --broker=amqp://root:w9jTwtNi1wm4Q3VPUfBecPWd@myrabbit:5672// --address=0.0.0.0  -port=5555