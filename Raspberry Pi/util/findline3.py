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

class findline3:
	# class memebers:
	kernel = np.ones((7,7), np.uint8)

	# Object constructor:
	def __init__(self,img):
		self._img = np.copy(img)
		self._raw = np.copy(img)
		self.RES = config.RES
		self.num = config.NUMofCUT
		self.xs =  config.CUTHEIGHT
		# print('cut:',self.xs)
		self.tol = config.tol
		self.CENTER = config.CENTER

	def markline(self, stdev=300):
		t0 = time.perf_counter()
		gimg = cv2.cvtColor(self._img,cv2.COLOR_BGR2GRAY)
		cimg = cv2.GaussianBlur(gimg, (3, 3), 0)

		self.midpoints = []
		self.midpoints.append(stdev)

		for i in range(0,self.num):
			r = len(self.midpoints)-1
			h = self.xs[i]
			cut = cimg[h].astype(np.int16)
			cut[cut > 150] = 150
			df = np.diff(cut)
			Lpt = np.where(df > 8)
			Rpt = np.where(df < -8)
			RR = len(Rpt[0])-1

			midpoint = int((Lpt[0][0]+Rpt[0][RR])/2)
			cv2.circle(self._img, (midpoint, h), 8, (0,255,0), -1)
			print('iteration = ',i)
			print('CUTHEIGHT: =', h)
			cv2.imshow('viewer',self._img)
			cv2.waitKey(0)
		return self.midpoints, self._img