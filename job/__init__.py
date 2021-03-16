# -*- coding: utf-8 -*- 
# @Time: 3/16/21 3:26 下午 
# @Author: xiaxiang
# @Desc:  celery 定时人物目录，可以与 web 程序结合实现异步或者 定时任务的处理

from celery import Celery
from core import app
from core.configs.config_base import Config
from job import settings


def make_celery(app, name):
    celery = Celery(name, broker=Config.BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)
    celery.config_from_object("job.settings")
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery_job = make_celery(app, 'celery_job')
