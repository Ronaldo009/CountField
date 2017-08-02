#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 下午3:10
# @Author  : Huang HUi
# @Site    : 
# @File    : contact_csv.py
# @Software: PyCharm
import csv

with open("/Users/yanfa/PycharmProjects/genPlanByDFS/result1.csv",'r') as csvin1,open("/Users/yanfa/PycharmProjects/genPlanByDFS/result2.csv",'r') as csvin2,open("result_finally.csv",'w') as csvout:
    csvreader1=csv.reader(csvin1)
    csvreader2=csv.reader(csvin2)
    csvwriter=csv.writer(csvout)
    next(csvreader1,None)
    next(csvreader2,None)
    csvwriter.writerow(['isGot','Path','Time','Query'])
    for row in csvreader1:
        if row[0]=="True":
            csvwriter.writerow([row[0],row[1],row[2],row[3]])
    for rows in csvreader2:
        csvwriter.writerow([rows[0],rows[1],rows[2],rows[3]])




