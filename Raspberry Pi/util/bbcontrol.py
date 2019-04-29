#!/usr/bin/python3
'''
Class definition for control system

'''
import numpy as np

class control:

	def __init__(self):
		print('Controller initialized!')

	def detlevel(self, pts, mapcond):
		lev = 0
		if mapcond == 0:
			npts = self.outlier_reject(pts[1:])
			devi = np.mean(npts) - 320
			if devi < 20 and devi > -20:
				lev = 0
			elif devi < -20:
				lev = -1
			else:
				lev = 1
		return lev

	def outlier_reject(self, pts,tol = 2.):
		d = np.abs(pts - np.median(pts))
		mdev = np.median(d)
		s = d/(mdev if mdev else 1.)
		return data[s<m]

