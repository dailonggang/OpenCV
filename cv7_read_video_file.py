"""
OpenCV读取mp4视频文件
"""

# 导入OpenCV
import cv2
import time

# 使用cv2.VideoCapture，参数换成文件名
cap = cv2.VideoCapture('./save_video/1.mp4')

# 首先加一个判断，如果文件不存在或编码错误提示
if not cap.isOpened():
    print('文件不存在或编码错误')

while cap.isOpened():
    # 读取帧
    ret, frame = cap.read()

    if ret:
        # 视频未播放完毕进行显示
        cv2.imshow('demo', frame)

        # 降低显示速度
        time.sleep(0.1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 视频播放完毕直接跳出
    else:
        break

cap.release()
cv2.destroyAllWindows()