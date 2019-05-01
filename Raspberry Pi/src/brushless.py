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
	y = "s"+str(x)
	a.sendmsg(y)
	time.sleep(2)

