import time
import sys
import os

sys.path.append(os.path.abspath('..'))
from dev.arduino import arduino

a = arduino()
a.sendmsg("i")
print("Initialization ")
time.sleep(6)
while True:
	x = input('Input the speed')
	x = int(x)

	if x <= 10:
		a.sendmsg("s10")
		time.sleep(2)

	if x >= 80:
		a.sendmsg("s60")
		time.sleep(2)
		a.sendmsg("s80")
		time.sleep(2)
		if x >= 100:
			a.sendmsg("s100")
			time.sleep(2)
			if x >= 120:
				a.sendmsg("s120")
				time.sleep(0)
