# Technical Report on Image Processing

## Abstract
In this chapter, we will introduce our vision based line following system. We use USB webcam to capture the images and process them on the Raspberry Pi Model 3 B+ single board controller. To increase the controllability of our robotic car, our system is designed to reach at least 10fps with fast and robust algorithm. The image is pre-processed by Gaussian low pass filter and some basic morphological processing technique to remove unwanted noise. The line will be detected by gradient-based method. Instead of using the whole image, we select limited number of slices (row vector) for faster computation. The advantage of visual sensors is that it enable our robotic car to predict future condition which buys more time for us to steer, especially at sharp turn. We will elaborate on the implementation details and provide some analysis in this chapter, including image processing technique and coding style.

