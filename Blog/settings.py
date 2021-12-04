#-*-codeing=utf-8 -*-
#@Time :2021/9/8 20:33
#@Author :Csn
#@File:settings
#@Software:PyCharm
#基础设置 数据库设置 跨站请求 数据库迁移
ENV='development'

DEBUG=True

SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1:3306/blogdb'
SQLALCHEMY_TRACK_MODIFICATIONS=True
SECRET_KEY='ASDFGHJK123456789ZXCVBN'
#python manage.py runserver
