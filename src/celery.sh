#!/bin/sh
# celery

rm -rf *.pid &&
celery multi start worker_youngtrip worker -A youngtrip -l info &&
celery beat -A youngtrip