import numpy as np
import matplotlib.pyplot as plt
import cv2

# 显示图片
img = cv2.imread('./img/dog.jpg')
while True:
    # 一直显示
    cv2.imshow("dog", img)
    # 如果至少等待10秒，按Esc键退出，ord('q')
    if cv2.waitKey(10) & 0xFF == 27:
        break

# 关闭所有窗口
cv2.destroyAllWindows()