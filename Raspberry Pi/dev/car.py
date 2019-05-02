#!/usr/bin/python3
# This is the class definition for "car"
# which provides user interface for steering.

import RPi.GPIO as GPIO
import time
import sys
import os

sys.path.append(os.path.abspath('..'))
from config import config
from dev.arduino import arduino

class car:
	angle = 0
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(config.SERVO_PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(config.SERVO_PIN, config.PWM_FREQ)
		self.pwm.start(0)

	def ang2pwm(self,angle):
		DC = (0.05 * config.PWM_FREQ) + (0.19 * config.PWM_FREQ * angle / 180)
		return DC

	def setdir(self, val = 0):
		angle = val - 30
		self.DC = self.ang2pwm(angle)
		self.pwm.ChangeDutyCycle(self.DC)

	def setlev(self,lev):
		if lev == 0:
			self.setdir(83)
			print('Set servo to go straight')
		elif lev == 1:
			self.setdir(89)
			print('Set servo to turn right')
		elif lev == -1:
			self.setdir(70)
			print('Set servo to turn left')
		else:
			for i in range(0,50):
				self.setdir(60)
				print("Turning Left!!!")
				time.sleep(0.1)

			print('Set servo to turn left: MAX')

	def setspeed(self,val):
		signaller = arduino()
		msg = 'r'+ str(val)
		signaller.sendmsg(msg)

	def stopcar(self):
		self.setdir(0)
		GPIO.cleanup()
		quit()







