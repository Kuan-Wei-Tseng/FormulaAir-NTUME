#!/usr/bin/python3
# Class definition for serial communication with Arduino

import serial
import threading
import sys 
import os

sys.path.append(os.path.abspath('..'))
from config import config

class arduino:
	ser = serial.Serial('/dev/ttyACM0', 9600)
	def __init__(self):
		print('Arduino Serial Communication Starts!')

	def sendmsg(self,msg):
		msg_encode = msg.encode()
		self.ser.write(msg_encode)

	def readmsg(self):
		j1 = threading.Thread(target=self.waitmsg, daemon=True, args=())
		j1.start()
		msg = j1.join()
		return msg

	def waitmsg(self):
		while True:
			if(ser.in_waiting >0):
				line = self.ser.readline()
				if line in config.cmdlist:
					return line




