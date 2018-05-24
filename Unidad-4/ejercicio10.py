from __future__ import print_function
from random import random
from variables import procesoDePoisson

def main():
	#T = 10
	#lambda = 5
	I, s = procesoDePoisson(10, 5)
	print(I, s)

if __name__ == "__main__":
	main()
