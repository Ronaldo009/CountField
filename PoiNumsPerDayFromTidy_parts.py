#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/11 下午5:45
# @Author  : Huang HUi
# @Site    : 
# @File    : PoiNumsPerDayFromTidy_parts.py
# @Software: PyCharm
import csv
import matplotlib.pyplot as plt
with open("/Users/yanfa/Downloads/number-poi-per-day(3).csv",'r') as csvout:
    csvreader=csv.reader(csvout)
    next(csvreader,None)
    numberOfPoi=[]
    frequency=[]
    for row in csvreader:
        numberOfPoi.append(row[0])
        frequency.append(row[1])

    frequency.reverse()
    numberOfPoi.reverse()


# 标签
def autolabel(rects):
    for ii,rect in enumerate(rects):
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%s'% (mean_values[ii]),
            ha='center', va='bottom')


#输入数据
mean_values=frequency
bar_labels=[]
for i in numberOfPoi:
    bar_labels.append(i)
#绘制图形
x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()


autolabel(rects)

plt.ylabel("Frequency")
plt.xlabel("NumOfPoiPerDay")
plt.xticks(x_pos,bar_labels)
plt.title("The Frequency of Number of Poi Per Day ")

plt.show()