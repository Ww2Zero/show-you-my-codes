# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/26
# Time: 12:42
# Blog: Ww2zero.github.io
# Function description
#**第 0015 题：** 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
#
#   {
#        "1" : "上海",
#        "2" : "北京",
#        "3" : "成都"
#   }
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

    def saveToExcel(self, file_name):
        excel = xlwt.Workbook(encoding='utf8')
        table = excel.add_sheet(self.filename)

        for i in range(len(self.jsondata)):
            table.write(i, 0, i)
            table.write(i, 1, self.jsondata[str(i + 1)])
        excel.save(file_name)

if __name__ == '__main__':
    tx = txtToXls()
    tx.loadTxt('city.txt')
    tx.saveToExcel('city.xls')
