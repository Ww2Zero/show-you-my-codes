# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 15:55
# Blog: Ww2zero.github.io
# Function description
# **第 0013 题：** 用 Python 写一个爬图片的程序，爬 [这个链接里的日本妹子图片 :-)](http://tieba.baidu.com/p/2166231880)

# coding=utf-8

import urllib2
import urllib
import os

from bs4 import BeautifulSoup


class getIMGFromURL(object):
    def __init__(self):
        self.srclist = []
        self.soup = None
        self.downloadpath = None

    def setURL(self, url):
        content = urllib2.urlopen(url).read()
        self.soup = BeautifulSoup(content,"html.parser")

    def setRule(self, classname):
        '''
        设置图片的classname
        '''
        for img in  self.soup.find_all('img', classname):
            self.srclist.append(img['src'])

    def setDownlaodpath(self, savepath="downlaod"):
        self.downloadpath = savepath
        if not os.path.exists(savepath):
            os.mkdir(savepath)

    def downloadIMG(self):
        if self.srclist:
            print "Download image start .."
            for src in self.srclist:
                print 'Begin download image : %s ......' % src
                file_name = src.split("/")[-1]
                dist = os.path.join(self.downloadpath, file_name)
                urllib.urlretrieve(src, dist, None)
                print 'Download image %s Done.' % src
            print 'Download %d images done.' % len(self.srclist)
        else:
            print 'No Imges found !!!'


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    classname = 'BDE_Image'
    img = getIMGFromURL()
    img.setURL(url)
    img.setRule(classname)
    img.setDownlaodpath()
    img.downloadIMG()
