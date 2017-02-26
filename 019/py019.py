# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/26
# Time: 13:54
# Blog: Ww2zero.github.io
# Function description
#
# **第 0019 题：** 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
#
# 所示：
#
#     <?xml version="1.0" encoding="UTF-8"?>
#     <root>
#     <numbers>
#     <!--
#     	数字信息
#     -->
#
#     [
#     	[1, 82, 65535],
#     	[20, 90, 13],
#     	[26, 809, 1024]
#     ]
#
#     </numbers>
#     </root>

import xlrd
import codecs
from lxml import etree


class xlsToXml(object):

    def __init__(self):
        self.data = []

    def loadXls(self, xlsname):
        excel = xlrd.open_workbook(xlsname)
        table = excel.sheet_by_name('numbers')
        print table.nrows
        for i in range(table.nrows):
            self.data.append(table.row_values(i))

    def writeXml(self, xmlname):
        output = codecs.open(xmlname, 'w', 'utf-8')
        root = etree.Element('root')
        numbers_xml = etree.ElementTree(root)
        numbers = etree.SubElement(root, 'numbers')
        numbers.append(etree.Comment(u'数字信息'))
        numbers.text = str(self.data)
        output.write(etree.tounicode(numbers_xml.getroot()))
        output.close()

if __name__ == '__main__':
    xx = xlsToXml()
    xx.loadXls('numbers.xls')
    xx.writeXml('numbers.xml')
