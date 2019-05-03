import time
import sys
import os

sys.path.append(os.path.abspath('..'))
from dev.arduino import arduino
m = sys.argv[1]


a = arduino()
if m == '1':
	a.sendmsg("i")
	print("Initialization ")
	time.sleep(6)

while True:

	a.sendmsg("s60")
	print("Set speed to 60.")
	for i in range(0,3):
		a.sendmsg("s60")
		print(i)
		time.sleep(1)
	a.sendmsg("s80")
	print("Set speed to 80.")
	for i in range(0,4):
		a.sendmsg("s80")
		print(i)
		time.sleep(1)
	while True:
		#y = input('Input Target Speed:')
		# cmd = "s" + y
		a.sendmsg("s110")
		print("set 110")
		time.sleep(2)
		a.sendmsg("s105")
		print("set 105")
		time.sleep(2)
