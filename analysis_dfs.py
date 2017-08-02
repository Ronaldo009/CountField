#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 下午4:04
# @Author  : Huang HUi
# @Site    : 
# @File    : analysis_dfs.py
# @Software: PyCharm
import csv
import ast
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import re
from collections  import Counter

with open("/Users/yanfa/PycharmProjects/genPlanByDFS/result2.csv",'r') as csvOut,open("result_dfs.csv",'w') as csvRes:
    csvReader=csv.reader(csvOut)
    next(csvReader,None)
    all_count=0
    false_count=0
    true_count=0
    false_exceedTime_count=0
    countryIdTotalList=[]
    countryIdFalseList=[]
    timeLessThanThree_true=0
    solutionExistUnknown=0
    solutionExistFalse=0
    numOfCountryExceedOne=0
    numOfRegionExceedOne=0

    for row in csvReader:
         all_count+=1
         countryId = re.findall(r'\'country_id\': \d+', row[7])
         a = countryId[0].replace("'", "")
         b = a.replace(": ", "")
         c = b.replace("country_id", "")
         countryIdTotalList.append(int(c))
         if row[0]=="False":
            false_count+=1
            if int(row[1])>1:
                numOfCountryExceedOne+=1
            if int(row[2])>1:

                numOfRegionExceedOne+=1
            if row[5]=="unknown":
                solutionExistUnknown+=1
            if row[5]=="False":
                solutionExistFalse+=1

            if row[4]=="False":
                false_exceedTime_count+=1
            if ast.literal_eval(row[3])>6:
                countryId_false = re.findall(r'\'country_id\': \d+', row[7])
                a = countryId_false[0].replace("'", "")
                b = a.replace(": ", "")
                c = b.replace("country_id", "")
                countryIdFalseList.append(int(c))
         if row[0]=="True":
             true_count+=1
             if ast.literal_eval(row[3])<3:
                 timeLessThanThree_true+=1



    a=("%.2f") % (((false_count) / all_count) * 100) + "%"
    b=("%.2f") % (((true_count )/ all_count) * 100) + "%"
    c=("%.2f")%((false_exceedTime_count/false_count)*100)+'%'
    d=("%.2f")%((timeLessThanThree_true/true_count)*100)+'%'
    e=("%.2f")%((numOfCountryExceedOne/false_count)*100)+'%'
    f=("%.2f")%((numOfRegionExceedOne/false_count)*100)+'%'

    csvwriter=csv.writer(csvRes)
    csvwriter.writerow(['field','count','base_field','percentage'])
    csvwriter.writerow(['all_count',all_count,"None","None"])
    csvwriter.writerow(['false_count',false_count,"all_count",a])
    csvwriter.writerow(['true_count',true_count,"all_count",b])
    csvwriter.writerow(['false_exceedTime_count',false_exceedTime_count,"false_count",c])
    csvwriter.writerow(['timeLessThanThree_true',timeLessThanThree_true,'true_count',d])
    csvwriter.writerow(['numOfCountryExceedOne',numOfCountryExceedOne,'false_count',e])
    csvwriter.writerow(['numOfRegionExceedOne', numOfRegionExceedOne, 'false_count', f])

countryIDCounter_total=Counter(countryIdTotalList)
countryIdCounter_false=Counter(countryIdFalseList)

countryIdList_total=[]
countryIdCount_total=[]
country_dic = {}

for countryId,count in countryIDCounter_total.items():
    countryIdList_total.append(countryId)
    countryIdCount_total.append(count)
    country_dic[countryId]=count

countryIdList_false=[]
countryCount_false=[]
country_dic_false={}
for countryId_false,count_false in countryIdCounter_false.items():
    countryIdList_false.append(countryId_false)
    countryCount_false.append(count_false)
    country_dic_false[countryId_false]=count_false





red_data=[]
green_data=[]

for i in countryIdList_false:
    red_data.append(country_dic_false[i])
    green_data.append(country_dic[i]-country_dic_false[i])

f, (ax1) = plt.subplots(1, figsize=(10,10))
bar_width = 0.5
bar_l = [i+1 for i in range(len(red_data))]
tick_pos = [i+(bar_width/2) for i in bar_l]
ax1.bar(bar_l, red_data, width=bar_width,
        label='false_data', alpha=0.5, color='r')
ax1.bar(bar_l, green_data, width=bar_width,
        bottom=red_data, label='Ture_data', alpha=0.5, color='g')
plt.sca(ax1)
plt.xticks(tick_pos,countryIdList_false)
ax1.set_ylabel("Count")
ax1.set_xlabel("country_id")
plt.legend(loc='upper right')
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.grid()
plt.show()



def autolabel(rects):
    for ii, rect in enumerate(rects):
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2., 1.02 * height, '%s' % (mean_values[ii]),
                 ha='center', va='bottom')

#输入数据
mean_values=countryCount_false
bar_labels=[]
for i in countryIdList_false:
    bar_labels.append(str(i))

#绘制图形

x_pos=list(range(len(bar_labels)))
rects=plt.bar(x_pos,mean_values,align='center',alpha=0.5)
plt.grid()


autolabel(rects)

plt.ylabel("count")
plt.xlabel("country_id")
plt.xticks(x_pos,bar_labels)
plt.title("The Detail of NotGot's Count")

plt.show()