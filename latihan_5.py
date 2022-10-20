import numpy as np
import cv2

img = cv2.imread('images/color_ball.jpg')

cv2.imshow("Image Original", img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

for y in range(img.shape[0]):
	for x in range(img.shape[1]):
		if img[y,x,0] > 90 and img[y,x,0] > 120 and img[y,x,1] < 40:
			img[y,x] = img[y,x]
		else:
			img[y,x] = [0,0,0]


img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow("Image Filtered", img)

while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break