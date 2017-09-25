#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-7 下午9:09
# @Author  : Liping
# @Site    : 
# @File    : service-check.py
# @Software: PyCharm

import  commands
import  os
import  sys
tmp_dir="/tmp/ESCloud"
service_dict={
    "nova":["source /root/openrc && nova service-list"],
    "neutron":["source /root/openrc && neutron agent-list"],
    "cinder":["source /root/openrc && cinder service-list"],
    "rabbitmq":["rabbitmqctl cluster_status"],
    "crm":["crm status"]
}
def ServiceCheck():
    for k,v in service_dict.iteritems():
        outfile=os.path.join(tmp_dir,k+"-service"+".txt")
        with open(outfile, "a+") as f:
            for com in v:
                code,result=commands.getstatusoutput(com)
                if code==0:
                    f.write(result)
                else:
                    f.write('error occured'+'\n'+result)