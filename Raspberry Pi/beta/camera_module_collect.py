from time import sleep
from picamera import PiCamera
import sys

camera = PiCamera()
camera.resolution = (1024, 768)
camera.rotation = 180

# Camera warm-up time
sleep(1)
counter = 1;
name = sys.argv[1]
while(1):
	a = input("Next")
	if a == 'e':
		break  
	name = name + str(counter) + '.jpg'
	camera.capture(name)
	counter = counter + 1
