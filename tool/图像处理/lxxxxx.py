import os
try:
	import cv2
	import numpy as np
	from matplotlib import pyplot as plt
	import scipy
	import urllib
except:
	os.system("pip install numpy")
	os.system("pip install opencv-python")
	os.system("pip install matplotlib")
	os.system("pip install scipy")
	# os.system("pip install urllib")
	import numpy as np
	import cv2
	from matplotlib import pyplot as plt
	import urllib
	import scipy

# GrabCut
name = "C:/Study/github/Lookoop/Image/OpenCV/image/m_5.jpg" #(794, 688, 3)
img = cv2.imread(name)

# print(img.shape) # (500, 500, 3)
mask = np.zeros(img.shape[:2],np.uint8) # mask
h, w, _ =  img.shape

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (int(w * 0.1), int(h * 0.1), int(w * 0.9), int(h * 0.9))
# rect = (0, 0, w, h)

# print(rect)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis] # np.newaxis = None

plt.subplot(121), plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread(name), cv2.COLOR_BGR2RGB))
plt.title("original"), plt.xticks([]), plt.yticks([])
plt.show()	

# import os
# import urllib2
# try:
# 	import cv2
# 	import numpy as np
# 	# from matplotlib import pyplot as plt
# 	import scipy
# except:
# 	os.system("pip install numpy")
# 	os.system("pip install opencv-python")
# 	# os.system("pip install matplotlib")
# 	os.system("pip install scipy")
# 	# os.system("pip install urllib")
# 	import numpy as np
# 	import cv2
# 	# from matplotlib import pyplot as plt
# 	import scipy

# # GrabCut
# url = "http://lxa.kim/download/?download=20180911-211843-8890/m_2.jpg"
# req = urllib2.Request(url)
# ff = urllib2.urlopen(url)
# data = ff.read()
# name = "m_2.jpg"
# with open(name, "wb") as f:
# 	f.write(data)
# img = cv2.imread(name)
# print(img.shape) # (500, 500, 3)
# mask = np.zeros(img.shape[:2],np.uint8) # mask


# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)
# print(bgdModel)  
# """
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
#   0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
#   0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
# """
# rect = (60,90,970,1360)

# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
# img = img*mask2[:,:,np.newaxis] # np.newaxis = None
# cv2.imshow("img", img)
# cv2.waitKey()
# cv2.destroyAllWindows()