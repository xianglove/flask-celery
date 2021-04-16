# -*- coding: utf-8 -*- 
# @Time: 3/16/21 3:31 下午 
# @Author: xiaxiang
# @Desc: celery 配置文件 (celery 升级版本后，这里的配置都是小写，较低版本都是大写)
from job.schedule import beat_schedule

timezone = 'Asia/Shanghai'
task_ignore_result = True
result_expires = 60 * 60
task_store_errors_even_if_ignored = True
worker_concurrency = 20   # 并发 worker数
worker_prefetch_multiplier = 6
force_execv = True
max_tasks_per_child = 100       # 每个worker 最大处理任务数
task_serializer = 'json'
accept_content = ['json', ]
result_serializer = 'json'
imports = ('job.tasks',)


task_default_exchange = 'celery_job'
task_default_routing_key = 'celery_job'
task_default_exchange_type = 'direct'
task_default_queue = 'celery_job'
