FROM python:3.7

VOLUME [ "/app" ]

WORKDIR /app

ENV DB_ENGINE='mysql' \
    DB_NAME='youngtrip' \
    DB_USER='root' \
    DB_PASSWORD='w9jTwtNi1wm4Q3VPUfBecPWd' \
    DB_HOST='mysql' \
    DB_PORT='3306' \
    MEDIA_ROOT='/media/'

COPY ./requirements.txt /app

RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/ 

CMD bash