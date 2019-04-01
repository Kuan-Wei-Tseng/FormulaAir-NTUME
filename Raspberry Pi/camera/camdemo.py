# Image Processing and Machine Vision Unit
import numpy as np
import cv2
import sys
import time

t0 = time.perf_counter()

cap = cv2.VideoCapture(0)

RES = [640,480]
NUMofCUT = 10
CUTHEIGHT = np.linspace(RES[1]-10,10,num = NUMofCUT)
tol = 0.3 * RES[0]

CENTER = int(RES[0]/2)

kernel = np.ones((3,3), np.uint8)

while (True):
	ret, img = cap.read()
	gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# Noise Removal with 5*5 Gaussian Low Pass Filter
	cimg = cv2.GaussianBlur(gimg, (5, 5), 0)
	# Binarize the image with threshold = 100
	ret,bimg = cv2.threshold(cimg,100,255,cv2.THRESH_BINARY)
	# Remove the residual noise left in the binary image by Morphological Opening
	oimg = cv2.morphologyEx(bimg, cv2.MORPH_OPEN, kernel)
	midpoints = []

	for i in range(0,NUMofCUT):
		height = int(CUTHEIGHT[i])
		cut = oimg[height].astype(np.int16)
		df = np.diff(cut)
		points = np.where(np.logical_or(df > 200, df < -200))
		if len(points) > 0 and len(points[0]) > 1:
			midpoint = int((points[0][0] + points[0][1]) / 2)
			if i > 0 and abs(midpoints[i-1]-midpoint) > tol:
				midpoint = int((points[0][2] + points[0][3]) / 2)
				Lpt = points[0][2]
				Rpt = points[0][3]
			else:
				Lpt = points[0][0]
				Rpt = points[0][1]

			cv2.circle(img, (Lpt, height), 5, (0,0,255), -1)
			cv2.circle(img, (Rpt, height), 5, (0,0,255), -1)
			cv2.circle(img, (midpoint, height), 8, (0,255,0), -1)
			cv2.circle(img, (CENTER, height), 8, (255,0,0), -1)

			cv2.rectangle(img, (Lpt-15, height-15),(Rpt+15, height+15) , (228, 255, 109), 2)
			midpoints.append(midpoint)

	print (time.perf_counter()-t0)	
	cv2.imshow('My Image', img)
  	if cv2.waitKey(300) & 0xFF == ord('q'):
  		break

cv2.destroyAllWindows()
#cv2.imwrite('marked.bmp',img)
