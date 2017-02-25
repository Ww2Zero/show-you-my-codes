# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 16:57
# Blog: Ww2zero.github.io
# Function description
#
# 0014: 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#   {
#       "1":["张三",150,120,100],
#       "2":["李四",90,99,95],
#       "3":["王五",60,66,68]
#   }
# 请将上述内容写到 student.xls 文件中，如下图所示：
#
#![student.xls](http://i.imgur.com/nPDlpme.jpg)
#
import json
import xlwt


class jsonToExcel(object):
    """docstring for jsonToExcel"""

    def __init__(self):
        self.jsondata = None
        self.filename = None

    def loadJsonFile(self, jsonfilename):
        self.filename = jsonfilename.split('.')[0]

        with open(jsonfilename, 'r') as f:

            self.jsondata = json.load(f, encoding='UTF-8')

    def saveToExcel(self, file_name):
        excel = xlwt.Workbook(encoding='utf8')
        table = excel.add_sheet(self.filename)

        row = 0
        for key, value in self.jsondata.items():
            table.write(row, 0, key)
            r = 1
            for v in value:
                table.write(row, r, v)
                r += 1
            row += 1
        excel.save(file_name)

if __name__ == '__main__':
    jx = jsonToExcel()
    jx.loadJsonFile('student.txt')
    jx.saveToExcel('student.xls')
