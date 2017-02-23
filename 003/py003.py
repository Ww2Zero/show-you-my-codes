# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by Ww2Zero
# Blog: Ww2zero.github.io
########################
# Function description:
# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
########################

import string
import random
import redis


class ACRedis(object):
    """docstring for ACRedis"""

    def __init__(self):
        self.re = None
        self.config = {
            'host': 'localhost', 'port': '6379', 'db': '0'
        }

    def connectRedis(self):
        self.re = redis.Redis(**self.config)

    def InsertDatas(self, key_list):
        count = 1
        for key in key_list:
            self.re.set(count, key)
            count += 1


class ActivateCodes(object):
    """
    生成激活码
    """

    def __init__(self):
        #  字典域 由数字和字母（包括大小写）组成
        self.FIELD = string.digits + string.letters
        self.GENERATE = None

    def createCodes(self, codenumber=10, codesize=10):
        """
            生成codenumber组随机码,每组生成的码的长度为codesize
        """
        def getCode(codesize):
            """
                得到codesize位激活码
            """
            return "".join(random.sample(self.FIELD, codesize))
        self.GENERATE = [getCode(codesize) for i in range(codenumber)]
        return True

    def saveinRedis(self):
        re = ACRedis()
        re.connectRedis()
        re.InsertDatas(self.GENERATE)

if __name__ == "__main__":
    ac = ActivateCodes()
    ac.createCodes(200, 30)
    ac.saveinRedis()
