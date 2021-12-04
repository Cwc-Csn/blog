#-*-codeing=utf-8 -*-
#@Time :2021/9/8 20:29
#@Author :Csn
#@File:__init__.py
#@Software:PyCharm
#数据库定义
#SQLAlchemy采用简单的Python语言，提供高效和高性能的数据库访问，实现了完整的企业级持久模型。它的理念是，SQL数据库的量级和性能比对象集合重要，而对象集合的抽象又重要于表和行。
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()