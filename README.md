# mock
测试过程中的自己搭建的 基于 falsk的 mock 服务

初衷：
自己经常需要与第三方对接，但是第三方的测试维护情况堪忧，但是由于回归需要，需要依赖。
自己就搭了个 简单的 flask 的后端服务，用于平时的测试过程。
推荐自己部门的业务测试，自助添加 mock 接口数据。


python runserver.py 即可运行

项目结构:

core/__init__ 初始化工作
core/configs: 存放配置文件，包括数据库链接配置，消息任务中间件链接配置等
core/view: 接口入口层
core/const: 常量配置
job/schedule: 异步任务task调度 
job/settings: 异步任务初始化配置(包括：消息格式，时区等)
job/tasks: 异步任务代码逻辑层
  
定时任务 beat 进程启动方式：
   celery -A job.celery_job beat -l info 
   
定时任务 worker 进程启动方式：
   celery -A job.celery_job worker -l info
   
 