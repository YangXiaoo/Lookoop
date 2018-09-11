import matplotlib.pyplot as plt
import cv2



import urllib.request



url = "http://lxa.kim/download/?download=20180911-211843-8890/m_2.jpg"
ff = urllib.request.urlopen(url)
data = ff.read()
with open("m_2.jpg", "wb") as f:
	f.write(data)
img = cv2.imread("m_2.jpg")
plt.imshow(img)
plt.show()