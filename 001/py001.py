# -*- coding: utf-8 -*-
# __author__:Ww2zero

import random
import string
class ActivateCodes(object):
    """
    **第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
    """
    def __init__(self):
        #  字典域 由数字和字母（包括大小写）组成
        self.FIELD = string.digits + string.letters
        self.GENERATE = None

    def createCodes(self,codenumber=10, codesize=10):
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


    def writeInFile(self,file):
        """
            写入文件 并按顺序排列
        """
        count = 1
        for i in self.GENERATE:
            with open(file, "a") as boom:
                boom.write(str(count).rjust(3) + "  " + i + "\n")
            count += 1


if __name__ == '__main__':
    ac = ActivateCodes()
    ac.createCodes(200,30)
    ac.writeInFile("accodes.txt")
