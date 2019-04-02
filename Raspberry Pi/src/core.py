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
from util.findline import findline

class core:
	# Object constructor:
	def __init__(self,mode):
		self.myCamera = camera()
		self.myCamera.activate()
		
		if not mode:
			demonstration()
		
		#img = self.myCamera.capture()
		#cv2.imwrite('test.bmp',img)

	def demonstration(self):
		while True:
			img = self.myCamera.capture()
			self.myFinder = findline(img)
			self.pts,self.mimg = self.myFinder.markline()
			cv2.imshow(self.pts)


			



