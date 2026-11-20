import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

# 检查是否成功打开摄像头
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 循环读取摄像头的每一帧图像
while True:
    # 从摄像头中获取一帧图像
    ret, frame = cap.read()

    # 检查是否读取成功
    if not ret:
        print("无法获取图像")
        break

    # 显示图像
    cv2.imshow("USB Camera", frame)

    # 等待按下 ESC 键退出
    if cv2.waitKey(1) == 27:
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
