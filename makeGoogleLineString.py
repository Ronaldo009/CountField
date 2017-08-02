#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 下午12:46
# @Author  : Huang HUi
# @Site    : 
# @File    : makeGoogleLineString.py
# @Software: PyCharm
import pymysql
import csv
import math
import sys

# google fusionTables
#encoding=utf-8
connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 db='uniqueway_development',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 charset='utf8')
with connection.cursor() as cursor:
    sql="select id,name from regions"
    cursor.execute(sql)
    regions=cursor.fetchall()
regionDic={}
for region in regions:
    id=region['id']
    regionDic[id]=region

import random
def makeColor():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())
colorDic={}
def getColorByCountry(country):
    if country in colorDic:
        return colorDic[country]
    else:
        color=makeColor()
        colorDic[country]=color
        return colorDic[country]



with open("/Users/yanfa/Downloads/regionToRegion2.csv",'r') as csvIn,open("result_Google_FustionTables.csv",'w',encoding='utf-8') as csvOut:
    csvReader=csv.reader(csvIn)
    next(csvReader,None)
    csvWriter=csv.writer(csvOut)
    csvWriter.writerow(['regionId','name','country','color','coordinates','frequency','width'])
    for row in csvReader:
        regionId=row[0]+"->"+row[3]
        name=regionDic[int(row[0])]['name']+"->"+regionDic[int(row[3])]['name']
        country=row[7]
        color=getColorByCountry(country)
        coordinates=u'<MultiGeometry><LineString><coordinates>'+row[2]+u','+row[1]+u',0.0 '+row[5]+u','+row[4]+u',0.0</coordinates></LineString></MultiGeometry>'
        frequency=row[6]
        width=2*round(math.log10(int(frequency)))
        csvWriter.writerow([regionId,name,country,color,coordinates,frequency,width])
