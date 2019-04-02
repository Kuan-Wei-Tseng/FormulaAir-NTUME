#!/usr/bin/python3
#This is the main entrance of the program.

from core import core
import sys

def main(mode):
	input("press ENTER to start:")
	if mode == "run":
		runner = core(True)
	elif mode == "demo":
		runner = core(False)
	else:
		print("To run or to demonstrate??")
	return

if __name__ == "__main__":
	main(sys.argv[1])