# -*- coding: utf-8 -*-
# __author__:Ww2zero
from PIL import Image, ImageDraw, ImageFont


class AddNumToPic(object):
    """
    第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
    """

    def __init__(self):
        self.font = None
        self.img = None

    def open(self, img_path):
        '''
        打开需要修改的图片
        img_path:需要修改的图片路径
        '''
        self.img = Image.open(img_path)
        return True

    def set_font(self, font_path, size):
        '''
         设置字体的路径和字体的大小
         font_path:字体的路径
         size:字体的大小
        '''
        self.font = ImageFont.truetype(font_path, size)
        return True

    def draw_text(self, str, color, ttf):
        '''
        在图片中绘制字符
        str：需要在图片中绘制的字符
        color：绘制的字符的颜色
        ttf：绘制的字符的字体

        draw.text((x,y),str,fill=color, font=font) 主要的绘制函数
            (x,y) 绘制的字符的位置(0,0)表示左上角
            str   需要绘制的字符
            color 颜色
            font  字体
        '''
        xSize, ySize = self.img.size
        fontSize = min(xSize, ySize) / 10.0
        # 使字符绘制在图片的右上角的位置
        position = (xSize - fontSize, fontSize)
        draw = ImageDraw.Draw(self.img)
        draw.text(position, str, fill=color, font=ttf)
        self.img.show()
        self.img.save("finnal" + str + '.' + self.img.format)
        return True

if __name__ == '__main__':
    pic = AddNumToPic()
    pic.open('tx.jpg')
    pic.set_font('msyh.ttf', 20)
    pic.draw_text('6', 'red', pic.font)
