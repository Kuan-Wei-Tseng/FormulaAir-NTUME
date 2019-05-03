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
	x = input('Input command')
	x = int(x)

	if x <= 10:
		a.sendmsg("s10")
		time.sleep(2)
	else:
		a.sendmsg("s60")
		print("Set speed to 60.")
		for i in range(0,3):
			print(i)
			time.sleep(1)
		a.sendmsg("s80")
		print("Set speed to 80.")
		for i in range(0,4):
			print(i)
			time.sleep(1)
		while True:
			y = input('Input Target Speed:')
			cmd = "s" + y
			a.sendmsg(cmd)
			time.sleep(2)
