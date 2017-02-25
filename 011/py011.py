# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 15:11
# Blog: Ww2zero.github.io
# Function description
#
#**第 0011 题：** 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。


def filteredWords(f_file):
    fWords = []
    with open(f_file) as f:
        for line in f:
            fWords.append(line.strip())
    return fWords


def checkFilteredWords(input, ffile):
    fwlist = filteredWords(ffile)
    if input in fwlist:
        print "Freedom"
    else:
        print "Human Rights"

if __name__ == "__main__":
    inputwords = raw_input("please input your word:")
    checkFilteredWords(inputwords, "filtered_words.txt")
