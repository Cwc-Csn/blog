#-*-codeing=utf-8 -*-
#@Time :2021/9/15 19:11
#@Author :Csn
#@File:blog
#@Software:PyCharm
#关于网页博客相关的功能函数
from  flask import Blueprint,request,session,redirect,url_for,render_template
import urlpath
from apps.models.blogmodels import User,Blog,Like
from exts import db
from sqlalchemy import or_
blog_bp=Blueprint('blog',__name__,url_prefix='/blog')

#1发布博客
@blog_bp.route('/publish/',methods=['GET','POST'])
def publish():
    if request.method=='GET':
        if session.get('username'):
            return render_template('publish.html')
        else:
            urlpath.current_url=url_for('blog.publish')
            return redirect(url_for('user.login'))
    else:
        print(request.form)
        user=User.query.filter(User.username==session.get('username')).first()
        title=request.form.get('title')
        content=request.form.get('content')
        blog=Blog(title,content,user.uid)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('index'))

@blog_bp.route('/index/')
def blogindex():
    #查询所有博客
    blogs=Blog.query.all()

    return render_template('index.html',blogs=blogs)
@blog_bp.route('/newindex/')
def blognewindex():
    #查询所有博客

    #blogs=Blog.query.all()
    # 分页
    curpage = int(request.args.get('curpage', 1))
    paginate = Blog.query.paginate(page=curpage, per_page=3)

    if session.get('username'):
        user=User.query.filter(User.username==session.get('username')).first()
        like_bids=[blog.bid for blog in user.like_blogs ]
        return render_template('new_index.html',paginate=paginate,like_bids=like_bids)

    else:
        like_bids=int('')
        return render_template('new_index.html',paginate=paginate,like_bids=like_bids)
@blog_bp.route('/like/')
def like():
    if session.get('username'):

        user=User.query.filter(User.username==session.get('username')).first()
        bid=int(request.args.get('bid'))
        blog=Blog.query.get(bid)
        like=Like(user.uid,bid)

        db.session.add(like)
        db.session.commit()
        return redirect(url_for('blog.blogindex'))
    else:
        urlpath.current_url=url_for('blog.blogindex')
        return redirect(url_for('user.login'))
@blog_bp.route('/unlike/')
def unlike():
    user = User.query.filter(User.username == session.get('username')).first()
    bid = int(request.args.get('bid'))
    blog = Blog.query.get(bid)
    like=Like.query.filter(Like.bid==bid,Like.uid==user.uid).first()
    db.session.delete(like)
    db.session.commit()
    return redirect(url_for('blog.blogindex'))

#点赞，取消点赞请求
@blog_bp.route('/likeorunlike/')
def likeorunlike():
    # if session.get('username'):
        bid=int(request.args.get('bid'))
        blog = Blog.query.get(bid)
        user = User.query.filter(User.username == session.get('username')).first()
        flag=False

        for like_user in blog.like_users:
            if like_user.username==session.get('username'):
                #取消点赞
                flag=True

                break
        if flag is True:
            # 取消点赞
            like=Like.query.filter(Like.uid==user.uid,Like.bid==bid).first()
            db.session.delete(like)
            db.session.commit()
            return {'code': 201, 'likenum': len(blog.like_users)}
        else:
            #d点赞
            like=Like(user.uid,bid)
            db.session.add(like)
            db.session.commit()
        # return redirect(url_for('blog.blognewindex'))
            return {'code':200,'likenum':len(blog.like_users)}

    # else:
    #     urlpath.current_url = url_for('blog.blogindex')
    #     return redirect(url_for('user.login'))

#点击用户名进入对应主页
@blog_bp.route('/userindex/')
def userindex():
    username=request.args.get('name')
    user=User.query.filter(User.username==username).first()


    return render_template('userindex.html',blogs=user.blogs)
#搜索博客
@blog_bp.route('/search/')
def search():
    search_content=request.args.get('search')

    blogs=Blog.query.filter(or_(Blog.title.contains(search_content),Blog.content.contains(search_content))).all()


    return render_template('search.html',blogs=blogs)

#sc删除博客
@blog_bp.route('/deleteblog',methods=['POST'])
def deleteblog():
    bid=int(request.form.get('bid'))
    blog=Blog.query.get(bid)
    db.session.delete(blog)
    db.session.commit()
    return '删除成功'