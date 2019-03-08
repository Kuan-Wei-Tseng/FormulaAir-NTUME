# Image Processing and Machine Vision Unit
import numpy as np
import cv2

kernel = np.ones((3,3), np.uint8)

img = cv2.imread('image.jpg')
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Noise Removal with 5*5 Gaussian Low Pass Filter
cimg = cv2.GaussianBlur(gimg, (5, 5), 0)
# Binarize the image using Automatic thresholding. (Otsu's method)
ret,bimg = cv.threshold(cimg,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Remove the residual noise left in the binary image by Morphological Opening
oimg = cv2.morphologyEx(bimg, cv2.MORPH_OPEN, kernel)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
