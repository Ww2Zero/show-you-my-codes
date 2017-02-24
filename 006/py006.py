# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/2/24
# Time: 15:01
# Blog: Ww2zero.github.io
# Function description
# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import glob
from collections import Counter
import re
import os


class diaryWords(object):
    def __init__(self):
        self.path = None
        self.importWords = []

    def setpath(self, path):
        self.path = path

    def setimportwords(self, words):
        self.importWords.append(words)

    def printDiaryWords(self):
        print u'日记路径：%s \n' % (self.path)
        print u'日记出现多的单词：%s \n' % (self.importWords)
        print u'-------------------------'


class countDiary(object):
    def __init__(self, path):
        self.path = path
        self.filepathlist = []
        self.datalist = []
        self.result = None
        self.diaryWords = None

    def openPath(self):
        for root, directories, files in os.walk(self.path):
            for filename in files:
                filepath = os.path.join(root, filename)
                self.filepathlist.append(filepath)
        return self.filepathlist

    def openFile(self, filename):
        self.datalist = []
        with open(filename, 'r') as wordfile:
            for line in wordfile:
                # 将符号替换成空格
                content = re.sub("\"|,|\.", "", line)
                # 1->去除首尾空格
                # 2->采用空格切分句子
                # 3->将切出的列表保存在datalist中
                self.datalist.extend(content.strip().split())

    def countWords(self):
        self.result = None
        self.result = Counter(self.datalist)

    def theMostImportWords(self, wordnumber=3):
        dwords = []
        for words in self.result.most_common(wordnumber):
            dwords.append(words)

        return dwords

    def printResult(self):

        for path in self.openPath():
            dw = diaryWords()
            dw.setpath(path)
            self.openFile(path)
            self.countWords()
            dw.setimportwords(self.theMostImportWords())
            dw.printDiaryWords()

if __name__ == "__main__":
    cd = countDiary('diary')
    cd.printResult()
