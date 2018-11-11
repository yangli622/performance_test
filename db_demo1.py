#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Administrator
@file:db_demo1.py
@create_time:2018/10/28
"""

from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# article 表：
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null,
# )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('articles'))

db.create_all()


@app.route('/')
def base_index():
    return redirect('/index')


@app.route('/index')
def index():
    # # 增加
    # article = Article(title='aaa', content='bbb')
    # db.session.add(article)
    # # 事务
    # db.session.commit()

    # # 查
    # # select * from article where title='aaa';
    # result = Article.query.filter(Article.title == 'aaa').first()
    # print result.title
    # print result.content

    # 改
    # # 1. 先把要更改的数据查出来
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2. 修改数据
    # article1.title = 'new_title'
    # # 3. 事务提交
    # db.session.commit()

    # # 删
    # # 1. 查找需要删除的数据
    # article1 = Article.query.filter(Article.title == 'new_title').first()
    # # 2. 删除数据
    # db.session.delete(article1)
    # # 3. 提交事务
    # db.session.commit()

    # # 要添加一篇文章，必须要有用户存在，首先创建一个用户
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()

    # article = Article(title='aaa', content='hello world', author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # # 要找文章标题为aaa的作者
    article = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print user.username

    # article = Article(title='aaa', content='hello world')
    # article.author = User.query.filter(User.id == 1).first()
    # db.session.add(article)
    # db.session.commit()

    # author = User.query.filter(User.username == 'zhiliao').first()
    # print author.articles
    # 要找文章标题为aaa的作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print 'username:', article.author.username

    # 要找到zhiliao这个用户的所有文章
    # article = Article(title='111', content='222', author_id=1)
    # db.session.add(article)
    # db.session.commit()
    user = User.query.filter(User.username == 'zhiliao').first()
    result = user.articles
    for article in result:
        print 'title', article.title
        print 'content', article.content

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)