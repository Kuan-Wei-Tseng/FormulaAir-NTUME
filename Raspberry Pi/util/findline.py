#!/usr/bin/python3
# This is the image processing unit for finding
# black line to trace in the given image.

import numpy as np
import cv2
import time
import sys
import os

sys.path.append(os.path.abspath('..'))
from config import config

class findline:
	# class memebers:
	kernel = np.ones((3,3), np.uint8)

	# Object constructor:
	def __init__(self,img):
		self._img = np.copy(img)
		self.RES = config.RES
		self.num = config.NUMofCUT
		self.xs =  np.copy(config.CUTHEIGHT)
		self.tol = config.tol
		self.CENTER = config.CENTER

	def markline(self,stdev=240):
		t0 = time.perf_counter()
		gimg = cv2.cvtColor(self._img,cv2.COLOR_BGR2GRAY)
		cimg = cv2.GaussianBlur(gimg, (5, 5), 0)
		ret,bimg = cv2.threshold(cimg,100,255,cv2.THRESH_BINARY)
		oimg = cv2.morphologyEx(bimg, cv2.MORPH_OPEN, self.kernel)
		self.midpoints = []
		self.midpoints.append(stdev)

		for i in range(0,self.num):
			self.needcheck = False
			h = self.xs[i]
			cut = oimg[h].astype(np.int16)
			df = np.diff(cut)
			points = np.where(np.logical_or(df > 200, df < -200))
			if len(points) > 0 and len(points[0]) == 2 and abs(self.midpoints[i]-int((points[0][0] + points[0][1]) / 2)) <= self.tol:
				Lpt = points[0][0]
				Rpt = points[0][1]
				midpoint = int((points[0][0] + points[0][1]) / 2)
			else:
				self.needcheck = True
				print('Need to Confirm')

			if self.needcheck:
				block = oimg[h-5:h+5].astype(np.int16)
				proj = np.sum(block,0)
				u = np.where(proj== min(proj))[0]
				print(i)
				print(self.midpoints[i])
				u = abs(u - self.midpoints[i])

				midpoint = np.argmin(u)
				if abs(self.midpoints[i]-midpoint) > self.tol:
					print('Cannot find the black line!')
					continue

			self.midpoints.append(midpoint)
			print('lenth of midpoints:')
			print(len(self.midpoints))
			cv2.circle(self._img, (midpoint, h), 8, (0,255,0), -1)
			cv2.circle(self._img, (self.CENTER, h), 8, (255,0,0), -1)

			if not self.needcheck:
				cv2.circle(self._img, (Lpt, h), 5, (0,0,255), -1)	
				cv2.circle(self._img, (Rpt, h), 5, (0,0,255), -1)
				cv2.rectangle(self._img, (Lpt-15, h-15),(Rpt+15, h+15) , (228, 255, 109), 2)
			else:
				cv2.rectangle(self._img, (midpoint-20, h-15),(midpoint+20, h+15) , (228, 255, 109), 2)

		print (time.perf_counter()-t0)
		return self.midpoints, self._img
















