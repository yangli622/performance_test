#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import Blueprint

main = Blueprint('main', __name__)

# 由于路由和错误处理页面定义在这个文件里面，导入到蓝本把他们关联起来，又因为views.py，error.py需要导入蓝本main，防止循环导入所以放到最后
from . import views, errors
