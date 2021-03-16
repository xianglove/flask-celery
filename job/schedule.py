# @Time: 3/16/21 3:45 下午
# @Author: xiaxiang
# @Desc:  配置定时任务调度
from datetime import timedelta
from celery.schedules import crontab

beat_schedule = {
    # 每 30秒执行一次。 秒级别可以用 timedelta, 分钟级别及以上可以用 crontab
    'task-one-function': {
        'task': 'job.tasks.task_one.task_one_function',
        'schedule': timedelta(seconds=30),
        'kwargs': {
        }
    },
    # 每周1早上8：20 分执行
    'task-two-function': {
        'task': 'job.tasks.task_one.task_two_function',
        'schedule': crontab(minute=20, hour=8, day_of_week=1)
    }
}
