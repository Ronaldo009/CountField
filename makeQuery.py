#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 下午4:04
# @Author  : Huang HUi
# @Site    : 
# @File    : makeQuery.py
# @Software: PyCharm
import pymysql
import csv
import ast
connection=pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           db='uniqueway_development',
                           cursorclass=pymysql.cursors.DictCursor,
                           charset='utf8'
                           )

# GIVEN_QUERY = {'days': [10,14], 'countries': [{'country_id': 28, 'day': None}],
#     'regions': [{'region_id': 2, 'day': None}, {'region_id': 27, 'day': None}, {'region_id': 69, 'day': None}], 'pois': [],
#     'regionNotGo': [], 'poiNotGo': [], 'regionSorted': [135, 131], 'availableMonths': [],
#     'price': [5000, 15000], 'hotelRating': None, 'arrivalRegionId': 27, 'departRegionId': None}


with connection.cursor() as cursor:
    sql="select * from gen_plan_search_logs where id>28000 and country_ids is not null"
    cursor.execute(sql)
    searchLog=cursor.fetchall()

    sql = "SELECT id, country_id, region_id, name FROM places"
    cursor.execute(sql)
    placeRecords = cursor.fetchall()

    places = {}
    for record in placeRecords:
        places[record['id']] = record
        places[record['id']].pop('id')

with open("Query2.csv",'w') as csvOut:
    csvWriter=csv.writer(csvOut)
    csvWriter.writerow(['sqlId','NumsOfCountry',"NumsOfRegion","Query"])
    count=0
    queryList=[]
    queryDicList=[]
    for row in searchLog:
        NumsOfCountry = 0
        NumsOfRegion = 0
        sqlId=row['id']
        if type(row['days'])==str:
            days=ast.literal_eval(row['days'])
        else:
            days=[]
        countryIds=ast.literal_eval(row['country_ids'])
        countries=[]
        for countryId in countryIds:
            NumsOfCountry+=1
            countryDic={'country_id':int(countryId),'day':None}
            countries.append(countryDic)
        regions=[]
        regionIdss = row['region_ids']
        regionSorted = []
        if regionIdss:
            print(type(regionIdss))
            print(id)
            regionIds=ast.literal_eval(regionIdss)
            for i in regionIds:
                NumsOfRegion+=1
                if row['is_in_order']:
                    regionSorted.append(int(i['id']))
                if i['day']:
                    day=int(i['day'])
                else:
                    day=None
                regionsDic={'region_id':int(i['id']),'day':day}
                regions.append(regionsDic)

        if row['poi_ids']:
            pois=ast.literal_eval(row['poi_ids'])
        else:
            pois=[]

        if row['disable_region_ids']:
            regionNotGo=[]
            for regionId in ast.literal_eval(row['disable_region_ids']):
                regionNotGo.append(int(regionId))
        else:
            regionNotGo=[]



        if row['disable_poi_ids']:
            poiNotGo=[]
            for poi in ast.literal_eval(row['disable_poi_ids']):
                poiNotGo.append(int(poi))
        else:
            poiNotGo=[]

        if row['available_month']:
            availableMonths=ast.literal_eval(row['available_month'])
        else:
            availableMonths=[]

        price=[]
        if row['min_price'] and row['max_price']:
            price=[int(row['min_price']),int(row['max_price'])]
        if not row['min_price'] and row['max_price']:
            price=[0,int(row['max_price'])]
        if row['min_price'] and not row['max_price']:
            price=[int(row['min_price']),80000]
        if not row['min_price'] and not row['max_price']:
            price=[]

        hotelRating=None
        arrivalRegionId=None
        if row['start_place_id']:
            arrivalRegionId=places[row['start_place_id']]['region_id']

        departRegionId=None
        if row['finish_place_id']:
            departRegionId=places[row['finish_place_id']]['region_id']

        query={'days':days,'countries':countries,'regions':regions,'pois':pois,'regionNotGo':regionNotGo,'poiNotGo':poiNotGo,
               'regionSorted':regionSorted,'availableMonths':availableMonths,'price':price,'hotelRating':hotelRating,'arrivalRegionId':arrivalRegionId,
               'departRegionId':departRegionId}


        if query not in queryList:
            count += 1
            queryList.append(query)
            csvWriter.writerow([sqlId,NumsOfCountry,NumsOfRegion,query])

            if count>5000:
                break






























