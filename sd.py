import cv2
import numpy as np
from matplotlib import pyplot as plt
#from matplotlib import pyplot as plt

img =cv2.imread("ph.jpg",0)

#cv2.imshow("Testing",img)
#cv2.waitKey(1000)

row=img.shape[0]
col=img.shape[1]
top=row*col

f=[]
b=[]

for i in range(0,256):
	f.append(0)
	b.append(i)

for i in range(0,row):
	for j in range(0,col):
		f[img[i,j]]=f[img[i,j]]+1

for i in range(0,256):
	f[i]=f[i]/top


plt.plot(b,f)
plt.show()
#for i in range(0,256):
#	print("f[",i,"] = ",f[i])

for i in range(0,row):
	for j in range(0,col):
		if img[i,j]<90:
			img[i,j]=0
		else:
			img[i,j]=255


cv2.imwrite("img5.png",img)
