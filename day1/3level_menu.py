#!/usr/bin/python27
#_*_ coding:utf-8 _*_

import sys,os,re,yaml,time
reload(sys)
sys.setdefaultencoding('utf-8')

dic = {"河南":{"南阳":["邓州市","镇平县","西峡县","新野县","唐河县"],
               "洛阳":["涧西区","西工区","偃师市","孟津县"],
               "周口":["川汇区","西华县","商水县","淮阳县"],
               "开封":["龙亭区","顺河区","鼓楼区","祥符区"],
             },
        "湖南":{"长沙":["芙蓉区","岳麓区","天心区","长沙县"],
                "益阳":["资阳区","赫山区","沅江市","安化县"]
               },
        "广东":{"深圳":["罗湖区","福田区","宝安区","盐田区","龙岗区"],
                "广州":["天河区","越秀区","白云区","黄埔区","番禺区"],
               }
       }

data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

flag=True

while flag:
    print "欢迎登录信息系统,b 返回 q 退出"
    province_dict={}
    for i,p in enumerate(data,1):
        province_dict[i]=p
        print i,p
    p_chose = raw_input("请输入查询省份:")
    # print data[province_dict[int(p_chose)]]
    if p_chose.isdigit():
        while flag:
            # print "请输入查询的城市:"
            city_dict={}
            for i,c in enumerate(data[province_dict[int(p_chose)]],1):
                city_dict[i]=c
                print i,c
            # print city_dict
            c_chose=raw_input("请输入查询城市,b返回上层，q退出:")
            if c_chose.isdigit():
                while flag:
                    # print "请输入查询的城市:"
                    xian_dict = {}
                    for i, x in enumerate(data[province_dict[int(p_chose)]][city_dict[int(c_chose)]], 1):
                        xian_dict[i] = x
                        print i, x
                    x_chose = raw_input("请输入查询县,b返回上层，q退出:")
                    if x_chose=='b':
                        break
            elif c_chose == 'b':
                break
            elif c_chose == 'q':
                flag = False
            else:
                print "你输入有误,请输入数字"
    elif p_chose=='b':
        print  "第一层，无法返回,请重新输入"
    elif p_chose=='q':
        flag=False
    else:
        print "你输入有误,请输入数字"