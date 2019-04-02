#!/usr/bin/python3
#Class definition for camera object.

import numpy as np
import cv2
import threading

class camera:
	# Object constructor:
	def __init__(self):
		print('USB web camera initializing...')
		self.cap = cv2.VideoCapture(0)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

	def capture(self):
		self.ret, self.frame = self.cap.read()
		return self.frame

	def close(self):
		self.cap.release()
