import cv2
import numpy as np

vid = cv2.VideoCapture(0)
params = cv2.SimpleBlobDetector_Params()

params.minThreshold = 100
params.minThreshold = 255

#Filter by alen
params.filterByArea = True
params.minArea = 500
params.maxArea = 250000

#filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.4

#filter by Convexcity
params.filterByConvexity = True
params.minConvexity = 0.3

#filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(Params)
else :
	detector = cv2.SimpleBlobDetector_create(params)

#define range of selected color in HSV
lower_limit = np.array([0,10,30])
upper_limit = np.array([30,255,255])

kernel =np.ones((5, 5), np.uint8)
while(True):

	#Capture the video frame
	# by frame
	_,im = vid.read()
	hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

	# Threshold the hsv image to get onl blue colors
	mask = cv2.inRange(hsv,lower_limit, upper_limit)
	mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	#biwise- And mask and origina image
	res = cv2.bitwise_and(im,im, mask= mask)

	#cv2.imshow('frame',im)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	#im3 = cv2.bitwise_not(im3)
	keypoints = detector.detect(cv2.bitwise_not(mask))

	#imcv = cv.cvtColor(np.aray(im),cv2.COLOR_RGB2BGR)
	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	#cv2.imshow("mask", im3)
	cv2.imshow("Detections", im_with_keypoints)

	#the 'q' button is set as the
	#quiting button you may use any
	#desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#after the loop reease the cap object
vid.release()
# destro all the windows
cv2.destroyAllWindows()
