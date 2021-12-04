#-*-codeing=utf-8 -*-
#@Time :2021/9/9 21:35
#@Author :Csn
#@File:user
#@Software:PyCharm
import os
import uuid
import basepath
from apps.models.blogmodels import User
from flask import Blueprint,request,render_template,redirect,url_for,session
from exts import db
import urlpath
user_bp=Blueprint('user',__name__,url_prefix='/user')
#关于网页 注册登录等 功能函数

#注册
@user_bp.route('/register/',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        name=request.form.get('username')
        psw=request.form.get('psw')
        phone=request.form.get('phone')

        user=User(name,psw,phone)
        db.session.add(user)
        db.session.commit()
        print(f'{request.form}')
        return redirect(url_for('user.login'))
@user_bp.route('/checkname/',methods=['POST'])
#检验用户名是否存在
def check_name():
    print(request.form)
    username=request.form.get('username')
    data=User.query.filter(User.username==username).first()
    print(data)
    if data:
        return {'code':2000,'msg':'用户名已存在'}
    else:
        return {'code': 2001, 'msg': '用户名不存在'}
    #无效代码
    return 'ok'

@user_bp.route('/checkphone/',methods=['POST'])
def check_phone():
    print(request.form)
    phone = request.form.get('phone')
    data = User.query.filter(User.phone == phone).first()
    print(phone)
    print(data)
    print(len(phone))
    if len(phone)!=11:
        return {'code': 2003, 'msg': '请输入正确的手机号'}
    else:
        if data:
            return {'code': 2003, 'msg': '手机号已注册'}
        else:
            return {'code': 2004, 'msg': '手机号没注册'}
@user_bp.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html',message='')
    else:
        username = request.form.get('username')
        psw = request.form.get('psw')
        user=User.query.filter(User.username==username,User.password==psw).first()
        if user is None:
            return render_template('login.html',message='用户名或者密码错误')
        else:
            #保存用户信息
            session['username']=username
            # session['user']=user
            print(session)
            return redirect(urlpath.current_url)

        return '登录成功'

@user_bp.route('/exit/')
def exit():
    session.pop('username')
    return redirect(url_for('index'))


#修改头像
@user_bp.route('/updateicon/',methods=['GET','POST'])
def updateicon():
    if request.method=='GET':
        return render_template('updateicon.html')
    else:
        icon_file=request.files.get('icon')
        if icon_file.filename !='':
            image_id=uuid.uuid4()
            dot_pos=icon_file.filename.rfind('.')
            image_name=str(image_id)+icon_file.filename[dot_pos:]
            save_path=os.path.join(basepath.basedir,'static\icon',image_name)
            icon_file.save(save_path)

            user=User.query.filter(User.username==session.get('username')).first()
            user.user_icon='icon/'+image_name
            db.session.commit()
        return redirect(url_for('blog.blogindex'))