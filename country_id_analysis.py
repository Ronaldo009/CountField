#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 上午10:44
# @Author  : Huang HUi
# @Site    : 
# @File    : country_id_analysis.py
# @Software: PyCharm

import csv
import ast
import operator
import matplotlib.pyplot as plt

with open("/Users/yanfa/PycharmProjects/genPlanBy_DFS/result.csv",'r') as csvread:
    csvreader=csv.reader(csvread)
    next(csvreader,None)
    count=0
    countryIdDic={}
    for row in csvreader:
        row[0]=ast.literal_eval(row[0])
        row[0]=list(map(int,row[0]))
        if str(row[0]) in countryIdDic:
            countryIdDic[str(row[0])]+=int(row[1])
        else:
            countryIdDic[str(row[0])] = int(row[1])

    countryIdDic=sorted(countryIdDic.items(),key=operator.itemgetter(1),reverse=True)

    print(countryIdDic[0:20])
    countryId=[]
    countryId_count=[]
    for i in countryIdDic[0:10]:
        countryId.append(i[0])
        countryId_count.append(i[1])

# 标签
def autolabel(rects):
    for ii,rect in enumerate(rects):
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%s'% (mean_values[ii]),
            ha='center', va='bottom')


#输入数据
mean_values=countryId_count
bar_labels=[]
for i in countryId:
    bar_labels.append(i)
#绘制图形
x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()


autolabel(rects)

plt.ylabel("Count")
plt.xlabel("Days")
plt.xticks(x_pos,bar_labels)
plt.title("The Count of Price From genPlan Search Log ")

plt.show()







