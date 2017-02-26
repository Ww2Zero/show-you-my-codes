# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/26
# Time: 13:12
# Blog: Ww2zero.github.io
# Function description
#**第 0017 题：** 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
#
# 下所示：
#
#     <?xml version="1.0" encoding="UTF-8"?>
#     <root>
#     <students>
#     <!--
#     	学生信息表
#     	"id" : [名字, 数学, 语文, 英文]
#     -->
#     {
#     	"1" : ["张三", 150, 120, 100],
#     	"2" : ["李四", 90, 99, 95],
#     	"3" : ["王五", 60, 66, 68]
#     }
#     </students>
#     </root>
#
# - [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 xml 和 Excel 相互转换

#-*- coding: utf-8-*-
import xlrd
import codecs
from lxml import etree


class xlsToXml(object):

    def __init__(self):
        self.data = {}

    def loadXls(self, xlsname):
        excel = xlrd.open_workbook(xlsname)
        table = excel.sheet_by_name('student')
        print table.nrows
        for i in range(table.nrows):
            key = str(int(table.row_values(i)[0]))
            # 获取编号后面的所有内容
            value = str(table.row_values(i)[1:])
            self.data[key] = value

    def writeXml(self, xmlname):
        output = codecs.open(xmlname, 'w', 'utf-8')
        root = etree.Element('root')
        students_xml = etree.ElementTree(root)
        students = etree.SubElement(root, 'students')
        students.append(etree.Comment(u'学生信息表\n\"id\": [名字，数学，语文，英语]'))
        students.text = str(self.data)
        output.write(etree.tounicode(students_xml.getroot()))
        output.close()

if __name__ == '__main__':
    xx = xlsToXml()
    xx.loadXls('student.xls')
    xx.writeXml('student.xml')
