# Webcam image previewer
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
name = '0422image'

for i in range(0,20):
	ret, frame = cap.read()
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		fname = name + str(i) + '.bmp'
		cv2.imwrite(fname,frame)
		continue

cap.release()
cv2.destroyAllWindows()