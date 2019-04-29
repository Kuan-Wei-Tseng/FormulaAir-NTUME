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
		
		if not mode:
			self.demonstration()
		else:
			self.run()
		
		#time.sleep(1)
		#img = self.myCamera.capture()
		#cv2.imwrite('test.bmp',img)

	def run(self):
		time.sleep(2)
		counter = 0
		while True:
			img = self.myCamera.capture()
			self.myFinder = findline(img)
			self.pts,self.mimg = self.myFinder.detectline()
			print(self.pts)
			counter = counter + 1
			if counter > 20:
				break

	def demonstration(self):
		time.sleep(2)
		counter = 0
		while True:
			img = self.myCamera.capture()
			self.myFinder = findline(img)
			self.pts,self.mimg = self.myFinder.detectline()
			print(self.pts)
			dev = self.mycontrol.detlevel(self.pts,self.maploc)
			print(dev)
			self.mycar.setlev(dev)
			self.mimg = self.myFinder.markline(self.pts)
			cv2.imshow('demo',self.mimg)
			if cv2.waitKey(0) == 27:
				break
			x = input('Save the image?')
			counter = counter + 1
			fname = '/home/pi/Desktop/debugimg' + str(counter) + '.bmp'
			if x == '1':
				cv2.imwrite(fname,img)
		cv2.destroyAllWindows()



			



