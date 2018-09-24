
import numpy as np  
import cv2  
import random
 
help_message ='''''USAGE: floodfill.py [<image>] 
Click on the image to set seed point 
Keys: 
  f     - toggle floating range 
  c     - toggle 4/8 connectivity 
  ESC   - exit 
'''  
  
if __name__ == '__main__':  
    import sys  
    try: fn = sys.argv[1]  
    except: fn = "C:\\Study\\test\\out_pic\\m_4.jpg" 
    print (help_message)  
  
    img = cv2.imread(fn, 0)  
    h, w = img.shape[:2]                 #得到图像的高和宽  
    mask = np.zeros((h+2, w+2), np.uint8)#掩码单通道8比特，长和宽都比输入图像多两
                                         #个像素点，满水填充不会超出掩码的非零边缘  
    seed_pt = None  
    fixed_range = True  
    connectivity = 4  
  
    def update(dummy=None):  
        if seed_pt is None:  
            cv2.imshow('floodfill', img)  
            return  
        flooded = img.copy()                      #以副本的形式进行填充，这样每次  
        mask[:] = 0                               #掩码初始为全0  
        lo = cv2.getTrackbarPos('lo', 'floodfill')#观察点像素邻域负差最大值  
        hi = cv2.getTrackbarPos('hi', 'floodfill')#观察点像素邻域正差最大值  
        flags = connectivity                      #低位比特包含连通值, 4 (缺省) 或 8  
        if fixed_range:  
            flags |= cv2.FLOODFILL_FIXED_RANGE    #考虑当前象素与种子象素之间的差（高比特也可以为0）  
        #以白色进行漫水填充  
        cv2.floodFill(flooded, mask, seed_pt, (255, 255, 255), 
                     (lo,)*3, (hi,)*3, flags)  
          
        # cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)#选定基准点用红色圆点标出  
        cv2.imshow('floodfill', flooded)  
        original = cv2.imread("C:\\Study\\test\\image\\m_4.jpg", 0)
        w, h = flooded.shape
        for i in range(w):
            for j in range(h):
                if flooded[i][j] != 0:
                    flooded[i][j] = 1

        res = np.multiply(flooded, original)
        cv2.imwrite("C:\\Study\\test\\out_pic\\m_4.jpg", res)
  
    def onmouse(event, x, y, flags, param):  #鼠标响应函数  
        global seed_pt  
        if flags & cv2.EVENT_FLAG_LBUTTON:   #鼠标左键响应，选择漫水填充基准点  
            seed_pt = x, y  
            update()  
  
    update()  
    cv2.setMouseCallback('floodfill', onmouse)  
    cv2.createTrackbar('lo', 'floodfill', 20, 255, update)  
    cv2.createTrackbar('hi', 'floodfill', 20, 255, update)  
  
    while True:  
        ch = 0xFF & cv2.waitKey()  
        if ch == 27:  
            break  
        if ch == ord('f'):  
            fixed_range = not fixed_range   #选定时flags的高位比特位0，也就是邻域的
                                            #选定为当前像素与相邻像素的的差，这样的效果就是联通区域会很大  
            print ('using %s range' % ('floating', 'fixed')[fixed_range])  
            update()  
        if ch == ord('c'):  
            connectivity = 12-connectivity  #选择4方向或则8方向种子扩散  
            print ('connectivity =', connectivity ) 
            update()  