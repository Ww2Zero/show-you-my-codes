# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/2/23
# Time: 15:15
# Blog: Ww2zero.github.io
# Function description
#  **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

from collections import Counter
import re


class CountWords(object):
    def __init__(self):
        self.datalist = []
        self.result = None
        pass

    def openFile(self, filename):
        with open(filename, 'r') as wordfile:
            for line in wordfile:
                # 将符号替换成空格
                content = re.sub("\"|,|\.", "", line)
                # 1->去除首尾空格
                # 2->采用空格切分句子
                # 3->将切出的列表保存在datalist中
                self.datalist.extend(content.strip().split())

    def countWords(self):
        self.result = Counter(self.datalist)

    def printResult(self):
        for words in self.result.most_common():
            print(words)


if __name__ == "__main__":
    cw = CountWords()
    cw.openFile('text.txt')
    cw.countWords()
    cw.printResult()
