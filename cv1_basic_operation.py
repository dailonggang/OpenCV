import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('./img/dog.jpg')
print(type(img))  # <class 'numpy.ndarray'>
img_transcol = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)  # 进行颜色三通道的改变
img_resize = cv2.resize(img_transcol, (500, 500))  # 尺寸变化
img_flip = cv2.flip(img_resize, flipCode=1)  # 0垂直翻转，1竖直翻转，-1原点翻转
plt.imshow(img_flip)  # opencv 对应通道为 B G R, matplotlib 对应通道为 R G B,所以显示的颜色有异
plt.show()

cv2.imwrite('./save_img/dog.jpg', cv2.cvtColor(img_flip, cv2.COLOR_RGB2BGR))