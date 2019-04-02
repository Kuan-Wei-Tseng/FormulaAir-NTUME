import numpy as np
import cv2
import time
import threading

def showimage():
    x = cv2.imread('marked.bmp')
    cv2.imshow('Hello',x)
    cv2.waitKey(5000)

#thread1 = threading.Thread(target=showimage, name='T1')
#thread1.start()


for i in range(0,10):
	x = cv2.imread('marked.bmp')
	print('Hello world')
	time.sleep(3)
	cv2.imshow('Hello',x)
	cv2.waitKey(1)