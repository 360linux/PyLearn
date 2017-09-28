#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-22 下午3:27
# @Author  : liping
# @File    : credentials.py
import os
import commands
import sys

def get_nova_creds():
    d = {}
    code, output = commands.getstatusoutput('source /root/openrc')
    if code == 0:
        d['username'] = os.environ['OS_USERNAME']
        d['api_key'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['project_id'] = os.environ['OS_TENANT_NAME']
        d['region_name']= os.environ['OS_REGION_NAME']
        return d
    else:
        print "failed to get nova creds,to exit"
        sys.exit(5)

