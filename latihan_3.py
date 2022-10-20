import numpy as np
import cv2

img = cv2.imread('images/color_ball.jpg')

cv2.imshow("Image", img)
#Read basic information
print (type(img))
print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#get pixel in BGR format
print (img[133,237,:])
print (img[188,466,:])
print (img[343,160,:])

while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break