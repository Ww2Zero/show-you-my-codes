# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/02/25
# Time: 14:17
# Blog: Ww2zero.github.io
# Function description
# **第 0010 题：**使用 Python 生成类似于下图中的**字母验证码图片**

# ![字母验证码](http://i.imgur.com/aVhbegV.jpg)

# - [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)
#

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


class checkImage(object):
    def __init__(self, fontsize=25):
        self.fontsize = fontsize
        self.width = int(fontsize * 1.5 * 4)
        self.height = int(fontsize * 1.5)
        self.image = None
        self.font = None
        self.draw = None

    def newImage(self):
        # create image instance
        self.image = Image.new(
            'RGB', (self.width, self.height), (255, 255, 255))
        # create font instance
        self.font = ImageFont.truetype("msyh.ttf", self.fontsize)
        # start ot draw
        self.draw = ImageDraw.Draw(self.image)

    def randomColor(self, colortype):
        '''
        colortype 0 代表背景颜色
                  1 代表字体颜色
        '''
        return (random.randint(125 * colortype, 125 * (colortype + 1)),
                random.randint(125 * colortype, 125 * (colortype + 1)),
                random.randint(125 * colortype, 125 * (colortype + 1)))

    def drawBackground(self):
        for x in range(self.width):
            for y in range(self.height):
                self.draw.point((x, y), fill=self.randomColor(0))

    def drawChar(self, charnumber=4):
        for t in range(charnumber):
            rchar = chr(random.randint(65, 90))
            self.draw.text((t * self.height + self.fontsize * 0.2, self.fontsize *
                            0.2), rchar, font=self.font, fill=self.randomColor(1))

    def show(self):
        self.newImage()
        self.drawBackground()
        self.drawChar()
        self.image.save('test.jpg')
        self.image.show()


if __name__ == '__main__':
    img = checkImage()
    img.show()
