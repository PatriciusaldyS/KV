import numpy as np
import cv2

def soal2() :
  img2 = cv2.imread('images/color_ball.jpg')
  width = img2.shape[0]
  height = img2.shape[1]
  for x in range(width) :
    for y in range(height) :
      b,g,r = img2[x, y]
      if( not( r == 255 and g == 255 and b == 255 ) and (r >= 235 and g >= 235 and b >= 235) ) :
        img2[x, y] = [0,0,0]
      else :
        img2[x, y] = [255,255,255]

  cv2.imshow('Soal 2', img2)

cv2.waitKey(0)
cv2.destroyAllWIndows()