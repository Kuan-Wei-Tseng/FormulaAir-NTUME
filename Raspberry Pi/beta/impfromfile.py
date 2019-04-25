#!/usr/bin/python3
# This problem is written for debugging and demonstration.
# It reads stored image and call the image processing program
# in ../util/findline2.py

import numpy as np
import cv2
import sys
import os

fname = sys.argv[1]
img = cv2.imread(fname)

sys.path.append(os.path.abspath('..'))
from util.findline2 import findline

worker = findline(img)
pts,img = worker.detectline()
worker.markline(pts)
