#-*-codeing=utf-8 -*-
#@Time :2021/9/8 20:32
#@Author :Csn
#@File:manage
#@Software:PyCharm

from flask_script import Manager
from flask import Flask, render_template, url_for,redirect
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from apps import create_app,models
from sqlalchemy import *
import migrate
from settings import SQLALCHEMY_DATABASE_URI
from apps.models import blogmodels
from apps.models.blogmodels import User
from exts import db
import urlpath
#程序运行主函数
#python manage.py runserver
app=create_app()

manager=Manager(app)

migrate=Migrate(app=app,db=db)

manager.add_command('database',MigrateCommand)

@app.route('/')
def index():
    urlpath.current_url=url_for('index')
    return redirect(url_for('blog.blogindex'))

if __name__=='__main__':
    manager.run()