#!/usr/bin/python3
# This is the class definition for "car"
# which provides user interface for steering.

import RPi.GPIO as GPIO
import time
import sys
import os

sys.path.append(os.path.abspath('..'))
from config import config

class car:
	angle = 0
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(SERVO_PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(SERVO_PIN, PWM_FREQ)
		self.pwm.start(0)

	def ang2pwm(self,angle):
		DC = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
		return DC

	def setdir(self, val = 0):
		angle = val
		if val > 90:
			angle = 90;
		elif val < -90:
			angle = -90;
		self.DC = self.ang2pwm(angle)
		self.pwm.ChangeDutyCycle(self.DC)

	def stopcar(self):
		self.setdir(0)
		GPIO.cleanup()
		quit()







