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

	def detectline(self, stdev=300):
		t0 = time.perf_counter()
		gimg = cv2.cvtColor(self._img,cv2.COLOR_BGR2GRAY)
		cimg = cv2.GaussianBlur(gimg, (5, 5), 0)
		ret,bimg = cv2.threshold(cimg,90,255,cv2.THRESH_BINARY)
		oimg = cv2.morphologyEx(bimg, cv2.MORPH_OPEN, self.kernel)
		oimg = cv2.morphologyEx(oimg, cv2.MORPH_CLOSE,self.kernel)
		self.midpoints = []
		self.midpoints.append(stdev)

		for i in range(0,self.num):
			r = len(self.midpoints)-1
			self.needcheck = False
			h = self.xs[i]
			cut = oimg[h].astype(np.int16)
			df = np.diff(cut)
			points = np.where(np.logical_or(df > 200, df < -200))
			print('iteration = ',i)
			print('CUTHEIGHT: =', h)
			print('len of points[0]: ',len(points[0]))

			if len(points) > 0 and len(points[0]) == 2:
				if i == 0:
					Lpt = points[0][0]
					Rpt = points[0][1]
					midpoint = int((points[0][0] + points[0][1]) / 2)
					print('Safe')
				else:
					if abs(self.midpoints[r]-(points[0][0] + points[0][1])/2) <= self.tol:
						Lpt = points[0][0]
						Rpt = points[0][1]
						midpoint = int((points[0][0] + points[0][1]) / 2)
						print('Safe')

			else:
				self.needcheck = True
				print('Need to Confirm')

			if self.needcheck:
				cut = cimg[h].astype(np.int16)
				cut[cut > 160] = 160
				df = np.diff(cut)
				Lpt = np.where(df < -8)
				Rpt = np.where(df > 8)
				if len(Lpt[0]) < 1 or len(Rpt[0]) <1:
					midpoint = np.argmin(cut)
				else:
					RR = len(Rpt[0])-1
					midpoint = int((Lpt[0][0]+Rpt[0][RR])/2)

				if abs(self.midpoints[r]-midpoint) > self.tol:
					print('Cannot find the black line!')
					x = input('Save? 1 = Yes.')
					if x == '1':
						naming = 'debugger' + str(i) + '.bmp'
						namer = 'rawimage' + str(i) +'.bmp'
						cv2.imwrite(naming,self._img)
						cv2.imwrite(namer,self._raw)
						print('Debug image saved')
					continue

			self.midpoints.append(midpoint)
			'''
			cv2.circle(self._img, (midpoint, h), 8, (0,255,0), -1)
			cv2.circle(self._img, (self.CENTER, h), 8, (255,0,0), -1)

			if not self.needcheck:
				cv2.circle(self._img, (Lpt, h), 5, (0,0,255), -1)	
				cv2.circle(self._img, (Rpt, h), 5, (0,0,255), -1)
				cv2.rectangle(self._img, (Lpt-15, h-15),(Rpt+15, h+15) , (228, 255, 109), 2)
			else:
				cv2.rectangle(self._img, (midpoint-20, h-15),(midpoint+20, h+15) , (228, 255, 109), 2)

			cv2.imshow('viewer',self._img)
			cv2.waitKey(0)
			'''

		print (time.perf_counter()-t0)
		return self.midpoints, self._img

	def markline(self,pts):
		for i in range(0,self.num):
			h = self.xs[i]
			midpoint = pts[i]
			cv2.circle(self._img, (midpoint, h), 8, (0,255,0), -1)

		cv2.imshow('viewer',self._img)
		cv2.waitKey(0)
		x = input('filename:')
		if x == '0':
			return
		fname = '/Users/wayne/Desktop/'+x+'.bmp'
		cv2.imwrite(fname,self._img)

















