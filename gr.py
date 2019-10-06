import cv2
import numpy as np
#from matplotlib import pyplot as plt

img =cv2.imread("img1.png",0)

row=img.shape[0]
col=img.shape[1]

des=cv2.imread("img1.png",1)

#print(type(des),type(img))

for i in range(0,row):
	for j in range(0,col):
		if img[i,j]>=0 and img[i,j]<=80:
			r=0
			g=0
			b=255
		elif img[i,j]>80 and img[i,j]<=160:
			r=0
			g=255
			b=0
		else:
			r=255
			g=0
			b=0
		des[i,j,0]=r
		des[i,j,1]=g
		des[i,j,2]=b


#for pixel in img:
#	print()

cv2.imshow("Image",des)
cv2.waitKey(1000)
cv2.imwrite("img2.png",des)
#px=img[100,100]
#print(px)

print(img.shape)


