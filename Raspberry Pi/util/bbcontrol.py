#!/usr/bin/python3
'''
Class definition for control system

'''
import numpy as np
import sys
import os

sys.path.append(os.path.abspath('..'))
from config import config

class control:

	def __init__(self):
		print('Controller initialized!')

	def maplocation(self,pts):
		self.lowindex = config.C1
		self.uppindex = config.C2 + self.lowindex
		print(pts)
		lower = np.mean(pts[0:self.lowindex])
		upper = np.mean(pts[self.lowindex:self.uppindex-1])
		print(pts[self.lowindex:self.uppindex-1])
		print(lower)
		print(upper)
		print(upper-lower)
		if lower < 100 and abs(upper-lower) > 150:
			return False
		else:
			return False

	def detlevel(self, pts, mapcond):
		lev = 0
		if mapcond == 0 and not self.maplocation(pts[1:]):
			# npts = self.outlier_reject(pts[1:])
			npts = pts[1:]
			devi = np.mean(npts) - 300
			if devi < 40 and devi > -40:
				lev = 0
			elif devi < -40:
				lev = -1
			else:
				lev = 1

		elif mapcond != 0 or self.maplocation(pts[1:]):
			lev = -2
			mapcond = 1

		return lev,mapcond

	def outlier_reject(self, pts,tol = 20.):
		d = np.abs(pts - np.median(pts))
		mdev = np.median(d)
		s = d/(mdev if mdev else 1.)
		return pts[s<tol]

