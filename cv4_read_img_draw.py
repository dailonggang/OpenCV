import cv2
import matplotlib.pyplot as plt
import numpy as np

# Image是用来读取图像、Imagedraw用来绘图，Imagefont是用来调用字体
from PIL import Image, ImageDraw, ImageFont

"""在读取的图片上绘图"""
img = cv2.imread('./img/dog.jpg')
img_transcol = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.rectangle(img_transcol, (50, 20), (70, 60), (255, 0, 255), 5)
cv2.circle(img_transcol, (100, 50), 10, (0, 255, 0), 5)
# print(type(img_transcol))


def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 将numpy.ndarray转为PIL.Image
    # print(type(img))
    draw = ImageDraw.Draw(img)
    # print(type(draw))
    # 字体的格式
    fontStyle = ImageFont.truetype("./font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # np.asarrray将结构数据转化为numpy.ndarray


# 将返回值赋值给变量
img_transcol = cv2AddChineseText(img_transcol, '汪汪', (40, 80), textColor=(0, 255, 0), textSize=100)
plt.imshow(img_transcol)
plt.show()