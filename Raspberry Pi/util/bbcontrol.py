#!/usr/bin/python3
'''
Class definition for control system

'''
import numpy as np
import sys
import os
import time

sys.path.append(os.path.abspath('..'))
from config import config

class control:

	def __init__(self):
		print('Controller initialized!')

	def maplocation(self,pts):
		self.lowindex = config.C1
		self.uppindex = config.C2 + self.lowindex
		lower = np.mean(pts[0:self.lowindex])
		upper = np.mean(pts[self.lowindex:self.uppindex-1])
		print("lower")
		print(pts[0:self.lowindex])

		lowvect = np.diff(pts[0:self.lowindex])
		lowvectmean  = np.mean(lowvect)
		print("lowvec")
		print(lowvect)
		#print(pts[self.lowindex:self.uppindex-1])
		#print(lower)
		#print(upper)
		#print(upper-lower)
		if lower < 100 and abs(upper-lower) > 150:
			return False
		else:
			return False

	def detlevel(self, pts, mapcond):
		lev = 0
		if mapcond == 0:
			npts = self.outlier_reject(pts[1:])
			npts = pts[1:]
			devi = np.mean(npts) - 380
			if devi < 40 and devi > -20:
				lev = 0
			elif devi < -40:
				lev = -1
			else:
				lev = 1

		elif mapcond == 1:
			lev = 2
			mapcond = 1
			print("Find Sharp turn")

		return lev

	def outlier_reject(self,pts,tol = 1):
		cpts = np.copy(pts)
		s = np.std(pts)
		m = np.mean(pts)
		z = (pts-m)/s
		index = np.where(abs(z)>1)
		cpts = np.delete(cpts,index)
		return cpts

