from __future__ import print_function
from random import random
from math import log, exp

# va Weibull
#F(X)=1-exp(-alpha*(x**beta))

def vaWeibull(alpha, beta):
	u = random()
	x = (-log(1 - u) / float(alpha))**(1 / beta)

	return x

def esperanza_vaWeibull(n, alpha, beta):
	acc = 0
	for _ in range(n):
		acc += vaWeibull(alpha, beta)
	return acc/float(n)

def main():
	for n in [10, 100, 1000, 100000]:
		print('N = ', n, 'E(X)', esperanza_vaWeibull(n, 1, 1))

if __name__ == "__main__":
	main()
