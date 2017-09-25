#!/usr/bin/env python
# -*- coding: utf-8 -*-


product_list=[
    ('iphone',6000),
    ('mac',8000),
    ('pc',5000),
    ('python',90),
    ('linux',390)
]
buy_list=[]

salary=raw_input('请输入你的工资总额:')
if salary.isdigit():
    salary=int(salary)
else:
    print "your input is not digtal"

while True:
    for k,v in enumerate(product_list):
        print k,v
    buy_choose=raw_input('请输入购买的东西:')
    if buy_choose.isdigit():
        buy_choose=int(buy_choose)
        if buy_choose<len(product_list) and buy_choose>=0:
            p_item=product_list[buy_choose]
            if p_item[1]<=salary:
                buy_list.append(p_item)
                salary-=p_item[1]
                print "add %s into buylist,your curreent salary is %d"  %(p_item,salary)
            else:
                print '余额不足'
        else:
            print '你购买的东西%s不存在' %buy_choose

    elif buy_choose == 'q':
        print "----------shopping list---------"
        for p in buy_list:
            print p
        print '你的余额为 %d'  %salary
        exit()

    else:
        print  'invalid input'

