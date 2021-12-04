#-*-codeing=utf-8 -*-
#@Time :2021/9/8 20:29
#@Author :Csn
#@File:__init__.py
#@Software:PyCharm

from flask import Flask
import settings
from exts import db
#导入蓝图板块
from apps.views.user import user_bp
from apps.views.blog import blog_bp
from apps.models.blogmodels import User
from flask_wtf.csrf import CSRFProtect
#网页注册APP 关联网页相关功能函数，路由器？


def create_app():


    app=Flask(__name__,template_folder='../templates',static_folder='../static')

    app.config.from_pyfile('../settings.py')
    app.config.from_object(User)

    db.init_app(app)
    CSRFProtect(app)

   # CSRFProtect(app)
    #注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(blog_bp)

    return app