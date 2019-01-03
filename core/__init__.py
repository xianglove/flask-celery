# -*- coding: utf-8 -*-
from flask import Flask
# from configs.configs import Config
# from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    # app.configs.from_object(Config)  配置读取
    # db.init_app(app)  # 初始化 SQLAlchemy 链接池
    return app


app = create_app()
# db = SQLAlchemy()
