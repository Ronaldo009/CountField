#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/4 下午3:59
# @Author  : Huang HUi
# @Site    : 
# @File    : qq.py
# @Software: PyCharm
import math
aa="{'days': [], 'countries': [{'country_id': 28, 'days': None}], 'regions': [{'region_id': 27, 'days': None}, {'region_id': 70, 'days': None}, {'region_id': 2, 'days': None}, {'region_id': 767, 'days': None}], 'regionNotGo': [], 'pois': [9511, 1558], 'poiNotGo': [], 'price': [724, 38271]}"
import re
countryId=re.findall(r'\'country_id\': \d+',aa)
print(countryId)

for i in countryId:
    a=i.replace("'","")
    b=a.replace(": ", "")
    c=b.replace("country_id","")
    print(c)

isGot_count=10
count=300
v = ("%.2f") %( (isGot_count / count)*100)+"%"
print(v)

aa=str([2,3])
import ast
bb=ast.literal_eval(aa)
print(type(bb))

a=87048
b=round(math.log2(a))
print(b)
