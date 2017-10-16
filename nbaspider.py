# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 21:39
# @Author  : DX.Ssssssss
# @File    : nbaspider.py
# @Software: PyCharm Community Edition

import requests
import pandas
from bs4 import BeautifulSoup as bs

def get_one_pageurl(url):
    result = []
    res = requests.get(url)
    res.encoding = ('GBK')
    soup = bs(res.text, 'html.parser')
    conments = soup.select('#logPanel a')[:-5]
    for i in conments:
        result.append((i.text, i['href']))
    return result

def get_url(url):
    urllist = []
    url = 'http://www.nba98.com/nbalx/'
    res = requests.get(url)
    res.encoding = 'GBK'
    soup = bs(res.text,'html.parser')
    links = soup.select('.list_body a')
    for link in links:
        urllist.append('http://www.nba98.com' + link['href'])
    return urllist

if __name__ == "__main__":
    url = 'http://www.nba98.com/nbalx/'
    url2 = 'http://www.nba98.com/nbalx/list_175_{}.html'
    url_lists = []
    for i in get_url(url):
        url_lists.extend(get_one_pageurl(i))
    #print(url_lists)
    df = pandas.DataFrame(url_lists)
    df.to_excel('NBA.xlsx')


