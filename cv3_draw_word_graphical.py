import cv2
import numpy as np
import matplotlib.pyplot as plt
"""绘制几何图形"""

black_img = np.zeros(shape=(500, 500, 3), dtype=np.int16)  # 纯黑底图

# 画矩形
cv2.rectangle(img=black_img, pt1=(100, 100), pt2=(200, 200), color=(0, 255, 0), thickness=5)
# 画圆，thickness=-1为实心填充
cv2.circle(img=black_img, center=(150, 150), radius=100, color=(0, 255, 255), thickness=5)
cv2.circle(img=black_img, center=(250, 250), radius=100, color=(255, 255, 0), thickness=-1)
# 画线
cv2.line(img=black_img, pt1=(0, 0), pt2=(500, 500), color=(255, 255, 255), thickness=5)

"""添加文字"""
cv2.putText(img=black_img, text="python", org=(300, 300), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=4,
            color=(255, 0, 255), thickness=5, lineType=cv2.LINE_4)

"""绘制多边形"""
# 定义多边形顶点，这些顶点以二维数据形式存储
points = np.array([[200, 400], [400, 300], [200, 100], [0, 300]], dtype=np.int32)
# print(points)
# print(points.shape)
# 转换成三维数组格式
pts = points.reshape((-1, 1, 2))
# print(pts)
# print(pts.shape)
cv2.polylines(img=black_img, pts=[pts], isClosed=True, color=(255, 0, 255), thickness=10)

plt.imshow(black_img)
plt.show()