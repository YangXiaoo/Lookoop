# 2018-9-6
# 一些函数

cv2.imread(filepath,flags)
# filepath：要读入图片的完整路径
# flags：读入图片的标志 
# cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
# cv2.IMREAD_GRAYSCALE：读入灰度图片
# cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# dv2.destroyWindow(wname)
# cv2.waitKey顾名思义等待键盘输入，单位为毫秒，即等待指定的毫秒数看是否有键盘输入，若在等待时间内按下任意键则返回按键的ASCII码，程序继续运行。若没有按下任何键，超时后返回-1。参数为0表示无限等待。不调用waitKey的话，窗口会一闪而逝，看不到显示的图片。
# cv2.destroyAllWindow()销毁所有窗口
# cv2.destroyWindow(wname)销毁指定窗口


cv2.imwrite('1.png',img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
cv2.imwrite('1.png',img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
# 使用函数cv2.imwrite(file，img，num)保存一个图像。第一个参数是要保存的文件名，第二个参数是要保存的图像。可选的第三个参数，它针对特定的格式：对于JPEG，其表示的是图像的质量，用0 - 100的整数表示，默认95;对于png ,第三个参数表示的是压缩级别。默认为3.
# 注意:
# cv2.IMWRITE_JPEG_QUALITY类型为 long ,必须转换成 int
# cv2.IMWRITE_PNG_COMPRESSION, 从0到9 压缩级别越高图像越小。


# 彩色图像转为灰度图像
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
# 灰度图像转为彩色图像
img3 = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# cv2.COLOR_X2Y，其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS


# threshold：固定阈值二值化
# https://docs.opencv.org/3.2.0/d7/d4d/tutorial_py_thresholding.html
ret, dst = cv2.threshold(src, thresh, maxval, type)
# src： 输入图，只能输入单通道图像，通常来说为灰度图
# dst： 输出图
# thresh： 阈值
# maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
# type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV


# 轮廓查找
image, contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_TREE: 得到图像中轮廓的整体层次结构。若想得到最外面的轮廓，可以使用cv2.RETR_EXTERNAL
# cv2.CHAIN_APPROX_SIMPLE： 轮廓逼近方法
# 返回修改后的图片， 图像的轮廓以及它们的层次
# contours : 矩阵的四个点


# 绘图
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
# drawContours() 它的第一个参数是原始图像，第二个参数是轮廓，一个python列表，第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为-1时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度。