#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Administrator
@file:views.py
@create_time:2018/10/13
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import NameForm
from .. import db
from ..models import Tenant


@main.route('/', methods=['GET', 'POST'])   # 不同的蓝本装饰器不同
def index():
    return render_template('home.html', title="Tenant")


@main.route('/tenant', methods=['GET', 'POST'])
def tenant():
    tenants = Tenant.query.filter(Tenant.id != 'aaa').all()
    return render_template('tenant.html', title='Tenant', tenants=tenants)


@main.route('/tenant/add', methods=['POST'])
def tenant_add():
    form_data= request.form
    _tenant = Tenant(tenant_name=form_data.get('tenant_name'), project_id=form_data.get('project_id'),
                     ak=form_data.get('tenant_ak'), sk=form_data.get('tenant_sk'))
    db.session.add(_tenant)
    db.session.commit()
    return redirect('tenant')


@main.route('/performance_test', methods=['GET', 'POST'])
def performance_test():
    return render_template('performance_test.html', title='Test')

