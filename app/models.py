#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Administrator
@file:models.py
@create_time:2018/11/11
"""
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Tenant(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(64), unique=True)
    tenant_name = db.Column(db.String(64), unique=True)
    ak = db.Column(db.String(64), unique=True)
    sk = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.tenant_name


class Environment(db.Model):
    __tablename__ = 'environments'
    id = db.Column(db.Integer, primary_key=True)
    env_name = db.Column(db.String(64), unique=True)
    api_gateway = db.Column(db.String(16), unique=True)
    ecs_url_domain = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.env_name
