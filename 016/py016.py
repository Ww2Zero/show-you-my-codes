# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/26
# Time: 12:57
# Blog: Ww2zero.github.io
# Function description
#**第 0016 题：** 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

#   [
#   	[1, 82, 65535],
#   	[20, 90, 13],
#   	[26, 809, 1024]
#   ]
import json
import xlwt


class txtToXls(object):

    def __init__(self):
        self.jsondata = None
        self.filename = None

    def loadTxt(self, jsonfilename):
        self.filename = jsonfilename.split('.')[0]
        with open(jsonfilename, 'r') as f:
            self.jsondata = json.load(f, encoding='UTF-8')
            print self.jsondata

    def saveToExcel(self, file_name):
        excel = xlwt.Workbook(encoding='utf8')
        table = excel.add_sheet(self.filename)
        for i in range(len(self.jsondata)):
            for j in range(len(self.jsondata[i])):
                table.write(i, j, self.jsondata[i][j])
        excel.save(file_name)

if __name__ == '__main__':
    tx = txtToXls()
    tx.loadTxt('numbers.txt')
    tx.saveToExcel('numbers.xls')
