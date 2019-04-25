#!/usr/bin/python3
# Class definition for serial communication with Arduino

import serial
import threading

sys.path.append(os.path.abspath('..'))
from config import config

ser = serial.Serial(config.DEVNAME, 9600)

class arduino:
	def __init__(self):
		print('Arduino Serial Communication Starts!')

	def sendmsg(self,msg):
		msg_encode = msg.encode()
		ser.write(msg_encode)

	def readmsg(self):
		j1 = threading.Thread(target=self.waitmsg, daemon=True, args=())
		j1.start()
		msg = j1.join()
		return msg

	def waitmsg(self):
		while True:
			if(ser.in_waiting >0):
				line = ser.readline()
				if line in config.cmdlist:
					return line




