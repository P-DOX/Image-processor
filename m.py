import cv2

img1 = cv2.imread('g1.jpg')
img2 = cv2.imread('index.png')
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
img = cv2.addWeighted(img2, 0.3, roi, 0.7, 0) 
cv2.imshow('image', img) 
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols ]
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)
# invmask = cv2.bitwise_not(mask)
# # mask1=cv2.bitwise_and(img2,mask,mask=mask)
# img1_bg = cv2.bitwise_and(roi,roi,mask = invmask)
# img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
# final=cv2.add(img1_bg,img2_fg)

# cv2.imshow("mask",mask)
# cv2.imshow("img1_bg",img1_bg)
# cv2.imshow("img2_fg",img2_fg)
# cv2.imshow("final",final)
cv2.waitKey(0)
