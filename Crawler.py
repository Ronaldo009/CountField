#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 下午3:12
# @Author  : Huang HUi
# @Site    : 
# @File    : Crawler.py
# @Software: PyCharm

import requests
import codecs
from bs4 import BeautifulSoup
import re
import time
import ast
download_url="https://movie.douban.com/top250"

def download_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data=requests.get(url,headers).content
    return data
def main():
    url=download_url
    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html=download_page(url)
            movies,url=parse_html(html)
            # print(movies)
            # fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))

def parse_html(html):
    soup=BeautifulSoup(html)
    movie_list_soup=soup.find('ol',attrs={'class':'grid_view'})
    time.sleep(1)
    movie_name_list =[]

    for movie_li in movie_list_soup.find_all('li'):
        detail=movie_li.find('div',attrs={'class':'hd'})
        movie_name=detail.find('span',attrs={'class':'title'}).get_text()
        movie_bd=movie_li.find('div',attrs={'class':'bd'})
        span=movie_bd.select('span')
        print(span[-2])
        movie_star=movie_bd.find('span',attrs={'class':'rating_num','property':"v:average"}).get_text()
        movie_comment=movie_bd.find_all('span')[-2].get_text()
        print(movie_comment)
        movie_comment=ast.literal_eval(re.findall(r'\d+',movie_comment)[-1])
        movieDic={'name':movie_name,'star':movie_star,'num_comment':movie_comment}
        movie_name_list.append(movieDic)
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, download_url + next_page['href']

if __name__ == '__main__':
    main()