#!/usr/bin/python3

from lib import get_args
import os, sys


if __name__ == "__main__":
	print(f"Currently working directory is {os.getcwd()} - {get_args([])}")
	print("Hello")

	if len(sys.argv[1:]) == 0:
		sys.exit("Please provide some arguments!")

