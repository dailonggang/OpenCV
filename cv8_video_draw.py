"""
OpenCV 读取摄像头视频视频流，并在画面上绘制文字和图形
"""

# 导入OpenCV
import cv2
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np


# 绘制中文函数
def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "./font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


# 读取默认摄像头
cap = cv2.VideoCapture(0)

# 计算摄像头画面宽高
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 坐标计算
left_x = width // 8
left_y = height // 4

right_x = width // 8
right_y = height // 4

# 计时开始时间
start_time = time.time()

while True:
    # 读取每一帧
    ret, frame = cap.read()

    # 绘制矩形
    # cv2.rectangle(frame, (left_x, left_y), (left_x + right_x, left_y + right_y), (255, 0, 255), 10)
    cv2.rectangle(frame, (15, 15), (150, 100), (255, 0, 255), 5)
    """计算FPS"""
    # 读取图片结束时间
    now = time.time()
    fps = int(1 / (now - start_time))
    # 重新赋值计算
    start_time = now

    # 添加中文
    frame = cv2AddChineseText(frame, '帧率：' + str(fps), (20, 50), textColor=(0, 255, 0), textSize=30)

    # 显示画面
    cv2.imshow('demo', frame)

    # 退出条件
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
