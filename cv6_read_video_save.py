"""
OpenCV读取摄像头视频流显示并保存
"""

# 导入OpenCV
import cv2

# 使用VideoCapture读取摄像头，0表示笔记本自带摄像头，如果有多个摄像头可以换成其他数字
cap = cv2.VideoCapture(0)

# 四位视频编码MJPG、DIVX、X264
fourcc = cv2.VideoWriter_fourcc(*"DIVX")

# 视频帧率
fps = 20

# 摄像头画面实际大小
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

output = cv2.VideoWriter("./save_video/1.mp4", fourcc, fps, (width, height))
# 再使用cap.read()读取视频流，类似照片，他会以一帧帧的图片返回，所以我们需要用一个循环语句来一直获取
while True:
    # ret是bool类型，frame可以当作图像来处理，返回的是元组
    ret, frame = cap.read()
    # print("ret为{}" .format(ret))
    # print("frame为{}" .format(frame))

    # 镜像
    frame = cv2.flip(frame, 1)
    # 直接cv2.imshow('demo', frame)为彩色，当然也可以转变为其他颜色，例如灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 写入画面到文件
    output.write(frame)
    # 显示图像
    cv2.imshow('demo', frame)

    # 退出条件: ESC，当然你也可以利用ord()转换为任意键退出
    if cv2.waitKey(10) & 0xFF == 27:
        break

output.release()
# 因为前面设置了map句柄，在这里进行释放。句柄：直接调用改为间接调用
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()

