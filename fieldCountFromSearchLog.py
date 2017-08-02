#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/28 上午11:19
# @Author  : Huang HUi
# @Site    : 
# @File    : fieldCountFromSearchLog.py
# @Software: PyCharm

import pymysql
import csv
import re
from itertools import groupby
from operator import itemgetter
connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 db='uniqueway_development',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 charset='utf8')
with connection.cursor() as cursor:
    sql="select * from gen_plan_search_logs where id>28000 and country_ids is not null"
    cursor.execute(sql)
    logss=cursor.fetchall()

logsList=[]
logsDic={}
for i in logss:
    id=i['id']
    country_ids=i['country_ids']
    days=i['days']
    # if type(days)==str:
    #     days=days
    if days==None:
        days=str([str(-1),str(-1)])
    self_drive=i['self_drive']
    if self_drive==None:
        self_drive=-1
    max_price = i['max_price']
    if max_price==None:
        max_price=-1
    min_price=i['min_price']
    if  min_price==None:
        min_price=-1
    price=[min_price,max_price]
    logsDic={"id":id,"country_ids":country_ids,"days":days,"self_drive":self_drive,"price":str(price)}

    logsList.append(logsDic)

logsSortedByCountryID=sorted(logsList, key=itemgetter("country_ids"))
logsCountByCountryID=dict([(g,len(list(i['id'] for i in k))) for g,k in groupby(logsSortedByCountryID,key=lambda x:x['country_ids'])])

logsSortedByDays=sorted(logsList,key=lambda x:x["days"])
logsCountByDays=dict([(g,len(list(i['id'] for i in k)))for g,k in groupby(logsSortedByDays,key=lambda x:x["days"])])

logsSortedBySelfDrive=sorted(logsList,key=lambda x:x["self_drive"])
logsCountBySelfDrive=dict([(g,len(list(i['id'] for i in k))) for g,k in groupby(logsSortedBySelfDrive,key=lambda x:x["self_drive"]) ])

logsSortedByPrice=sorted(logsList,key=lambda x:x["price"])
logsCountByPrice=dict([(g,len(list(i['id'] for i in k))) for g,k in groupby(logsSortedByPrice,key=lambda x:x["price"])])

with open("countryIDCountSearchLog.csv",'w') as csvout:
    writer=csv.writer(csvout)
    writer.writerow(['country_id','Count'])
    for key,value in logsCountByCountryID.items():
        writer.writerow([key,value])

with open("daysCountSearchLog.csv",'w') as csvout:
    writer=csv.writer(csvout)
    writer.writerow(['days','Count'])
    for key,value in logsCountByDays.items():
        writer.writerow([key,value])

with open("selfDriveCountSearchLog.csv",'w') as csvout:
    writer=csv.writer(csvout)
    writer.writerow(['selfDrive','Count'])
    for key,value in logsCountBySelfDrive.items():
        writer.writerow([key,value])

with open("PriceCountSearchLog.csv",'w') as csvout:
    writer=csv.writer(csvout)
    writer.writerow(['Price','Count'])
    for key,value in logsCountByPrice.items():
        writer.writerow([key,value])


