#!/usr/bin/python3
'''
Class definition for faster camera object.
It creates a thread when camera capture begins.
The thread will keep grab frames from the camera
without decoding it. It will return the most recent
frame under core's request.
'''

import numpy as np
import cv2
import threading

class camera:
	# Object constructor:
	def __init__(self):
		print('USB web camera initializing...')
		self.status = True 
		self.frame = []
		self.cap = cv2.VideoCapture(0)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

	def activate(self):
		print('Buffer updater activated...')
		threading.Thread(target=self.bufferflush, daemon=True, args=()).start()

	def capture(self):
		self.ret,self.frame = self.cap.retrieve(self.gb)
		return self.frame

	def bufferflush(self):
		while self.status:
			self.gb = self.cap.grab()

		self.cap.release()

	def close(self):
		self.status = False
