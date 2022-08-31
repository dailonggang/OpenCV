"""
OpenCV读取摄像头视频流并进行显示
"""

# 导入OpenCV
import cv2

# 使用VideoCapture读取摄像头，0表示笔记本自带摄像头，如果有多个摄像头可以换成其他数字
cap = cv2.VideoCapture(0)

# 再使用cap.read()读取视频流，类似照片，他会以一帧帧的图片返回，所以我们需要用一个循环语句来一直获取
while True:
    # ret是bool类型，frame可以当作图像来处理，返回的是元组
    # 参数ret 为True 或者False,代表有没有读取到图片, 参数frame表示截取到一帧的图片
    ret, frame = cap.read()
    # print("ret为{}" .format(ret))
    # print("frame为{}" .format(frame))

    # 镜像
    frame = cv2.flip(frame, 1)
    # 直接cv2.imshow('demo', frame)为彩色，当然也可以转变为其他颜色，例如灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示图像
    cv2.imshow('demo', gray)

    # 退出条件: ESC，当然你也可以利用ord()转换为任意键退出
    if cv2.waitKey(10) & 0xFF == 27:
        break

# 因为前面设置了cap句柄，在这里进行释放。句柄：直接调用改为间接调用
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()