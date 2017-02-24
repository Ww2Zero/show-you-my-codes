# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 11:35
# Blog: Ww2zero.github.io
# Function description
# **第 0007 题：** 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来.

import os


class lineCounter(object):
    def __init__(self, path):
        self.path = path
        self.codelines = 0
        self.commentlines = 0
        self.emptylines = 0

    def linecounter(self):
        for root, directories, files in os.walk(self.path):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath) as code_file:
                    codeslines = code_file.readlines()
                    for line in codeslines:
                        line = line.strip()
                        if line.startswith("#"):
                            self.commentlines += 1
                        if line.startswith('//'):
                            self.commentlines += 1
                        elif line == "":
                            self.emptylines += 1
                        else:
                            self.codelines += 1

    def printResult(self):
        print u'%s目录中的代码统计如下' % (self.path)
        print u'代码行数为：%s' % (self.codelines)
        print u'注释行数为：%s' % (self.commentlines)
        print u'空行数为：%s' % (self.emptylines)


if __name__ == "__main__":
    lc = lineCounter('../../show-you-my-code')
    lc.linecounter()
    lc.printResult()
