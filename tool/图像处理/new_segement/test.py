# coding:UTF-8
import cv2
import numpy as np

img = cv2.imread("C:\\Study\\test\\1ssssssss\\m-10-11 (1).png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def func(algorithm, par=None):
    algorithms = {
        "SIFT" : cv2.xfeatures2d.SIFT_create(),
        "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
        "ORB": cv2.ORB_create()
    }
    return algorithms[algorithm]

f = "SIFT"
alg = func(f)
keypoints, descriptor = alg.detectAndCompute(gray, None)
points2f = cv2.KeyPoint_convert(keypoints) 
# print(points2f)
# print(keypoints)
dummy = np.zeros(gray.shape)
for i in points2f:
	# print(i[0], i[1])
	cv2.circle(dummy, tuple(i), 2, (51, 163, 236), 1) #33

# print(dummy.shape)
# img = cv2.drawKeypoints(image=img, outImage=dummy, keypoints=keypoints, color=(51, 163, 236))
# cv2.imshow(f, img)
cv2.imwrite("test.png", dummy)
# print(dummy.max())
cv2.waitKey()
cv2.destroyAllWindows()
