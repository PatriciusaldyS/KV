import numpy as np
import cv2

img = cv2.imread('images/kotak_kotak.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)
dst = cv2.cornerharris(gray,2,3,0.04)

d