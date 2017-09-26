#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-20 下午8:28
# @Author  : Liping
# @Site    : 
# @File    : credentials.py
# @Software: PyCharm

import os
import commands


def get_keystone_creds():
    d = {}
    code, status = commands.getstatusoutput("source /root/openrc")
    if code == 0:
        d['username'] = os.environ['OS_USERNAME']
        d['password'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['tenant_name'] = os.environ['OS_TENANT_NAME']
        d['region_name'] = os.environ['OS_REGION_NAME']
    return d


def get_nova_creds():
    d = {}
    code,status=commands.getstatusoutput("source /root/openrc")
    if code == 0:
        d['username'] = os.environ['OS_USERNAME']
        d['api_key'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['project_id'] = os.environ['OS_TENANT_NAME']
        d['region_name'] = os.environ['OS_REGION_NAME']
    return d
