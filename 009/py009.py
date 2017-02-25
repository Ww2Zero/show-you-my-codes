# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 12:30
# Blog: Ww2zero.github.io
# Function description
# **第 0009 题：**一个HTML文件，找出里面的**链接**。


from bs4 import BeautifulSoup
import requests

###requests.exceptions.ChunkedEncodingError:
import httplib
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

class htmlURLs(object):

    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,und;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

    def setURL(self, url):
        self.text = requests.get(url, headers=self.headers).text

    def getURLs(self):
        soup = BeautifulSoup(self.text, "html.parser")
        for alink in soup.find_all('a'):
            print alink
if __name__ == "__main__":
    url = "http://www.tensorfly.cn/home/"
    hu = htmlURLs()
    hu.setURL(url)
    hu.getURLs()
