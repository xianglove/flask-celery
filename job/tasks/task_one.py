# @Time: 3/16/21 3:51 下午
# @Author: xiaxiang
# @Desc:
from job import celery_job


@celery_job.task()
def task_one_function(xx=1, yy=2):
    # 可以在这里
    # 实现你的异步任务的逻辑
    print(111, 222)


@celery_job.task()
def task_two_function(*args, **kwargs):
    #  实现逻辑的代码模块
    print(1111)
