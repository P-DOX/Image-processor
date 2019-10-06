import cv2
import numpy as np

image = cv2.imread('./Images/one.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Creating our 3 x 3 kernel
kernel_3x3 = np.ones((3, 3), np.float32)/ 9

blurred = cv2.filter2D(image, -1, kernel_3x3)
cv2.imshow('3x3 Kernel Blurring', blurred)
cv2.waitKey(0)

# Creating our 8 x 8 kernel
kernel_8x8 = np.ones((8, 8), np.float32) / 64

blurred2 = cv2.filter2D(image, -1, kernel_7x7)
cv2.imshow('8x8 Kernel Blurring', blurred2)
cv2.waitKey(0)
cv2.destroyAllWindows()