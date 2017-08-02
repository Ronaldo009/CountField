#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/4 下午2:52
# @Author  : Huang HUi
# @Site    : 
# @File    : resCountField.py
# @Software: PyCharm

import pandas as pd

import csv
import re
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import ast

count=0
isGot_count=0
isNotGot_count=0
countryIdList=[]
countryIdTotalList=[]
numOfCountryList=[]
numOfCountryExceedOne_count=0
numOfCountryEqualOne_count=0
CountryEqualOne_totalCount=0
numOfunSolution=0
numOfTimeOut=0
numOfCountryPathNotExists=0
numOfRegionPathNotExists=0
OriginRegionList=[]
RecommendRegionsList=[]
RecommendAndOriginRegionsList=[]
csvReader=csv.reader(open('/Users/yanfa/Downloads/result(4).csv',encoding='utf-8'))
for row in csvReader:
    count+=1
    if row[1] == "1":
        numOfCountryEqualOne_count += 1
        countryId = re.findall(r'\'country_id\': \d+', row[15])

        a = countryId[0].replace("'", "")
        b = a.replace(": ", "")
        c = b.replace("country_id", "")
        countryIdTotalList.append(int(c))
    if row[0]=="1":
        isGot_count+=1

    if row[0]=="0":
        isNotGot_count+=1
        numOfCountryList.append(row[1])
        if int(row[1])>1:
            numOfCountryExceedOne_count+=1
        if row[1]=="1":
            numOfCountryEqualOne_count+=1
            countryId =re.findall(r'\'country_id\': \d+',row[15])

            a = countryId[0].replace("'", "")
            b = a.replace(": ", "")
            c = b.replace("country_id", "")
            countryIdList.append(int(c))
        if row[2]=="False":
            numOfunSolution+=1
            if row[3]=="False":
                numOfCountryPathNotExists+=1
            if row[4]=="False":
                numOfRegionPathNotExists+=1

        if row[7]=="True":
            numOfTimeOut+=1
            OriginRegionList.append(len(ast.literal_eval(row[9])))
            RecommendRegionsList.append(len(ast.literal_eval(row[10])))
            RecommendAndOriginRegionsList.append(len(ast.literal_eval(row[11])))


from collections import Counter
countryId_count=Counter(countryIdList)
countryId=[]
countList=[]
countryDic={}
for country_id,count in countryId_count.items():
    countryId.append(country_id)
    countList.append(count)
    countryDic[country_id]=count

OriginRegion=Counter(OriginRegionList)
RecommendRegions=Counter(RecommendRegionsList)
RecommendAndOriginRegions=Counter(RecommendAndOriginRegionsList)

OriginRegionlength=[]
OriginRegionCount=[]
for length,count in OriginRegion.items():
    OriginRegionlength.append(length)
    OriginRegionCount.append(count)

RecommendRegionlength=[]
RecommendRegionCount=[]
for length,count in OriginRegion.items():
    RecommendRegionlength.append(length)
    RecommendRegionCount.append(count)

RecommendAndOriginRegionslength=[]
RecommendAndOriginRegionsCount=[]
for length,count in OriginRegion.items():
    RecommendAndOriginRegionslength.append(length)
    RecommendAndOriginRegionsCount.append(count)

countryIds=Counter(countryIdTotalList)
countryIdss=[]
country_count=[]
countryIdDic={}
for countryId_name,count in countryIds.items():
    countryIdss.append(countryId_name)
    country_count.append(count)
    countryIdDic[countryId_name]=count




# 标签
def autolabel(rects):
    for ii,rect in enumerate(rects):
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%s'% (mean_values[ii]),
            ha='center', va='bottom')


red_data=[]
green_data=[]
for i in countryId:
    red_data.append(countryDic[i])
    green_data.append(countryIdDic[i]-countryDic[i])

f, (ax1) = plt.subplots(1, figsize=(10,10))
bar_width = 0.5
bar_l = [i+1 for i in range(len(red_data))]
tick_pos = [i+(bar_width/2) for i in bar_l]
ax1.bar(bar_l, red_data, width=bar_width,
        label='isNotGot', alpha=0.5, color='r')
ax1.bar(bar_l, green_data, width=bar_width,
        bottom=red_data, label='isGot', alpha=0.5, color='g')
plt.sca(ax1)
plt.xticks(tick_pos,countryId)
ax1.set_ylabel("Count")
ax1.set_xlabel("country_id")
plt.legend(loc='upper right')
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.grid()
plt.show()









#输入数据
mean_values=countList
bar_labels=[]
for i in countryId:
    bar_labels.append(str(i))
#绘制图形
x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()


autolabel(rects)

plt.ylabel("count")
plt.xlabel("country_id")
plt.xticks(x_pos,bar_labels)
plt.title("The Detail of numOfCountryEqualOne's Count")

plt.show()

#输入数据
mean_values=OriginRegionCount
bar_labels=[]
for i in OriginRegionlength:
    bar_labels.append(str(i))

#绘制图形
x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()


autolabel(rects)

plt.ylabel("count")
plt.xlabel("OriginRegionLength")
plt.xticks(x_pos,bar_labels)
plt.title("The Detail of OriginRegion's Count")

plt.show()

#输入数据
mean_values=RecommendRegionCount
bar_labels=[]
for i in RecommendRegionlength:
    bar_labels.append(str(i))

#绘制图形
x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()
# 标签
autolabel(rects)
plt.ylabel("count")
plt.xlabel("RecommendRegionLength")
plt.xticks(x_pos,bar_labels)
plt.title("The Detail of RecommendRegion's Count")
plt.show()


#输入数据
mean_values=RecommendAndOriginRegionsCount
bar_labels=[]
for i in RecommendAndOriginRegionslength:
    bar_labels.append(str(i))

#绘制图形
x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()
# 标签
autolabel(rects)
plt.ylabel("count")
plt.xlabel("RecommendAndOriginRegionsLength")
plt.xticks(x_pos,bar_labels)
plt.title("The Detail of RecommendAndOriginRegions's Count")
plt.show()













with open("countResult.csv",'w') as csvout:
    writer=csv.writer(csvout)
    writer.writerow(['Field',"count","BasedField","BasedField_count","Percent"])
    v=("%.2f") % ((isGot_count / count) * 100) + "%"
    m=("%.2f") % ((isNotGot_count / count) * 100) + "%"
    a=("%.2f") % ((numOfunSolution / isNotGot_count) * 100) + "%"
    b=("%.2f") % ((numOfTimeOut / isNotGot_count) * 100) + "%"
    c=("%.2f") % ((numOfCountryExceedOne_count / isNotGot_count) * 100) + "%"
    d=("%.2f") % ((numOfCountryEqualOne_count / isNotGot_count) * 100) + "%"
    e=("%.2f") % ((numOfCountryPathNotExists / numOfunSolution) * 100) + "%"
    f=("%.2f") % ((numOfRegionPathNotExists / numOfunSolution) * 100) + "%"

    writer.writerow(["isGot_count",isGot_count,"count",count,v])
    writer.writerow(["isNotGot_count",isNotGot_count,"count",count,m])
    writer.writerow(["numOfunSolution",numOfunSolution,"isNotGot_count",isNotGot_count,a])
    writer.writerow(["numOfTimeOut",numOfTimeOut,"isNotGot_count",isNotGot_count,b])
    writer.writerow(["numOfCountryPathNotExists",numOfCountryEqualOne_count,"numOfunSolution",numOfunSolution,e])
    writer.writerow(["numOfRegionPathNotExists",numOfRegionPathNotExists,"numOfunSolution",numOfunSolution,f])
    writer.writerow(["numOfCountryExceedOne_count",numOfCountryExceedOne_count,"isNotGot_count",isNotGot_count,c])
    writer.writerow(["numOfCountryEqualOne_count",numOfCountryEqualOne_count,"isNotGot_count",isNotGot_count,d])
    writer.writerow(["numOfCountryEqualOne_count",countryId_count,"None","None","None"])

