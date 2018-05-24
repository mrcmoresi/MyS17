from __future__ import print_function
from random import random
from math import exp, log
from variables import exponencial

def metodoRechazo():
	u = random()
	#Y ~Exp(1/2)
	v = random()
	y = exponencial(0.5)
	while u < (y/2.0)*exp((-1/2.0)*y+1):
		y = exponencial(0.5)
		u = random()

	return y

def esperanza(N):
	acc = 0
	for _ in range(N):
		acc += metodoRechazo()
	return acc/float(N)

def main():
	for N in [10, 100, 1000, 10000]:
		print('N = ', N, 'E(X) = ', esperanza(N))

if __name__ == "__main__":
	main()