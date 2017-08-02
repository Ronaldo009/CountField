#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 下午5:53
# @Author  : Huang HUi
# @Site    : 
# @File    : crawler_douban.py
# @Software: PyCharm

import requests

import requests
import re
import csv
import time
from bs4 import BeautifulSoup
url_first='https://movie.douban.com/top250'
res=requests.get(url_first)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')

def get_movie(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    grid_view = soup.find('ol', attrs={'class': 'grid_view'})
    li = grid_view.find_all('li')
    movie_all=[]
    for item in li:
        link = item.find('div', attrs={'class': 'hd'}).select('a')[0]['href']
        title = item.find('div', attrs={'class': 'hd'}).select('.title')[0].text
        bd = item.find('div', attrs={'class': 'bd'})
        year_style = bd.select('p')[0].text.splitlines()[2]
        year = year_style.split('/')[0]
        countyOrArea = '/'.join(year_style.split('/')[1].split(' '))
        style = '/'.join(year_style.split('/')[2].split(' '))
        rating = bd.select('.rating_num')[0].text
        comment_nums = re.findall(r'\d+', bd.select('.star')[0].select('span')[-1].text)[0]
        quote=None
        if bd.select('.inq'):
            quote =bd.select('.inq')[0].text


        print(title, year, countyOrArea, style, rating, comment_nums, quote, link)
        movie={'title':title,'year':year,'style':style,'rating':rating,'comment_nums':comment_nums,'quote':quote,'link':link,'country':countyOrArea}
        movie_all.append(movie)

    next = soup.find('span', attrs={'class': 'next'}).select('link')
    if next:
        return url_first+str(next[0]['href']),movie_all
    else:
        return [],movie_all

def get_allMovie():
    url = 'https://movie.douban.com/top250'
    with open('Top250_douban.csv','w',encoding='utf-8') as csvOut:
        csvwriter=csv.writer(csvOut)
        csvwriter.writerow(['Id','Title','Year','Style','Rating','Comments','Country','Quote','Link'])
        i=0
        while len(url)>0:
            url, movie_all = get_movie(url)
            time.sleep(1)
            for movie in movie_all:
                csvwriter.writerow([i,movie['title'],movie['year'],movie['style'],movie['rating'],movie['comment_nums'],movie['country'],movie['quote'],movie['link']])
                i+=1

if __name__ == '__main__':
    get_allMovie()











