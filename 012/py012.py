# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 15:11
# Blog: Ww2zero.github.io
# Function description
#
# **第 0012 题：** 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。


def filteredWords(f_file):
    fWords = []
    with open(f_file) as f:
        for line in f:
            fWords.append(line.strip())
    return fWords


def checkFilteredWords(input, ffile):
    fwlist = filteredWords(ffile)
    for word in fwlist:
        if input.find(word) != -1:
            text = input.replace(word, '**')
    print text

if __name__ == "__main__":
    inputwords = raw_input("please input your word:".decode('utf8'))
    checkFilteredWords(inputwords, "filtered_words.txt")
