#!/usr/bin/python3
# This is the handler program for all subsystems, 
# which should be called and initiated by main.py

import time
import numpy as np
import cv2
import sys
import os

sys.path.append(os.path.abspath('..'))
from dev.fastcamera import camera
from dev.car import car
from util.findline2 import findline
from util.bbcontrol import control

class core:
	# Object constructor:
	maploc = 0
	def __init__(self,mode):
		self.myCamera = camera()
		self.myCamera.activate()
		self.mycar = car()
		self.mycontrol = control()
		
		if mode == 2:
			self.demonstration()
		elif mode == 1:
			self.run()
		else:
			self.saveimg()
		
		#time.sleep(1)
		#img = self.myCamera.capture()
		#cv2.imwrite('test.bmp',img)

	def run(self):
		t0 = time.perf_counter()
		tt = 0
		time.sleep(2)
		counter = 0
		while True:
			self.maploc = 0
			img = self.myCamera.capture()
			self.myFinder = findline(img)
			self.pts,self.mimg, self.maploc = self.myFinder.detectline()
			print(self.pts)
			if tt < 10000
				self.maploc = 0
			dev = self.mycontrol.detlevel(self.pts,self.maploc)
			print(dev)
			if tt < 500:
				dev = 0
			self.mycar.setlev(dev)
			deltat = time.perf_counter()-t0
			tt = tt + deltat
			print("total time: %f" %tt)

			# self.mimg = self.myFinder.markline(self.pts)

	def demonstration(self):
		t0 = time.perf_counter()
		tt = 0
		time.sleep(2)
		counter = 0
		while True:
			img = self.myCamera.capture()
			self.myFinder = findline(img)
			self.pts,self.mimg, self.maploc = self.myFinder.detectline()
			#print(self.pts)
			if tt < 5000:
				self.maploc = 0
			dev = self.mycontrol.detlevel(self.pts,self.maploc)
			#print(dev)
			if tt < 500:
				dev = 0
			self.mycar.setlev(dev)
			self.mimg = self.myFinder.markline(self.pts)
			deltat = time.perf_counter()-t0
			tt = tt + deltat
			print(tt)
			cv2.imshow('demo',self.mimg)
			if cv2.waitKey(10) == 27:
				break
			'''
			x = input('Save the image?')
			counter = counter + 1
			fname = '/home/pi/Desktop/debugimg' + str(counter) + '.bmp'
			
			if x == '1':
				cv2.imwrite(fname,img)
			'''
		cv2.destroyAllWindows()

	def saveimg(self):
		time.sleep(2)
		counter = 0
		while True:
			img = self.myCamera.capture()
			fname = '/home/pi/Desktop/obstacle' + str(counter) + '.bmp'
			cv2.imshow('demo',img)
			if cv2.waitKey(0) == 27:
				break
			x = input('Save the image?')
			if x == '1':
				cv2.imwrite(fname,img)
				counter = counter + 1




			



