#!/usr/bin/python3

from lib import get_args
import os


if __name__ == "__main__":
	print(f"Currently working directory is {os.getcwd()} - {get_args([])}")
	print("Hello")
