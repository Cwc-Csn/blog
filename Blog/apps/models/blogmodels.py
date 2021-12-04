#-*-codeing=utf-8 -*-
#@Time :2021/9/11 20:37
#@Author :Csn
#@File:blogmodels
#@Software:PyCharm
#用户模型 数据库 表对应类
from flask import url_for

from  exts import db
#python manage.py database migrate
#python manage.py upgrade

class User(db.Model):
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False)

    phone=db.Column(db.String(11),unique=True)
    user_icon=db.Column(db.String(100))
    # , default = url_for('static', filename='icon/LenovoWallPaper.jpg')
    #f发布的博客
    blogs=db.relationship('Blog',backref='user')
    #dz点赞的博客
    like_blogs=db.relationship('Blog',secondary='like')
    def __init__(self,username,password,phone):
        self.username=username
        self.password=password
        self.phone=phone


class Blog(db.Model):
    bid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    thum_content = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    #外键
    uid=db.Column(db.Integer,db.ForeignKey('user.uid'))
    like_users=db.relationship('User',secondary='like')
    # like_usernames=[User.username for user in like_users]
    def __init__(self, title, content, uid):
        self.title = title
        self.content = content
        self.uid = uid
        self.thum_content=(content[0:100]+'......') if len(content)>100 else content

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid=db.Column(db.Integer,db.ForeignKey('user.uid'))
    bid=db.Column(db.Integer,db.ForeignKey('blog.bid'))

    def __init__(self,uid,bid):
        self.uid=uid
        self.bid=bid