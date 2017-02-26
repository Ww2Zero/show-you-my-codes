# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/26
# Time: 13:27
# Blog: Ww2zero.github.io
# Function description
#**第 0018 题：** 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
#
# <?xmlversion="1.0" encoding="UTF-8"?>
# <root>
# <citys>
# <!--
# 	城市信息
# -->
# {
# 	"1" : "上海",
# 	"2" : "北京",
# 	"3" : "成都"
# }
# </citys>
# </root>

import xlrd
import codecs
from lxml import etree


class xlsToXml(object):

    def __init__(self):
        self.data = {}

    def loadXls(self, xlsname):
        excel = xlrd.open_workbook(xlsname)
        table = excel.sheet_by_name('city')
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
        students = etree.SubElement(root, 'city')
        students.append(etree.Comment(u'城市信息'))
        students.text = str(self.data)
        output.write(etree.tounicode(students_xml.getroot()))
        output.close()

if __name__ == '__main__':
    xx = xlsToXml()
    xx.loadXls('city.xls')
    xx.writeXml('city.xml')
