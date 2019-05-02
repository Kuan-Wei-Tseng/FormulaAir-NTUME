#!/usr/bin/python3
#This is the main entrance of the program.

from core import core
import sys

def main(mode):
	input("press ENTER to start:")
	if mode == "run":
		runner = core(1)
	elif mode == "demo":
		runner = core(2)
	else:
		print("To run or to demonstrate??")
		runner = core(3)
	return

if __name__ == "__main__":
	main(sys.argv[1])