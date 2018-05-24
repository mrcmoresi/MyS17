from __future__ import print_function
from random import random
from math import sqrt

# Transformada Inversa
# F distribucion continua e inversible y U ~ U(0,1)
# ==> X = F^(-1)(U) v.a. con distribucion F
# P(X<=a) = P(F^(-1)(U)<=a) = P(F(F^(-1)(U))<=F(a)) = P(U<=F(a)) = F(a)


def ejercicio1():
	x = 0
	U = random()
	if U <= 0.25:
		x = 2+2*sqrt(U)
	else:
		x = 6-6*sqrt((1-U)/float(3))
	return x

def esperanza_ej1(n):
	acc = 0
	for _ in range(n):
		acc += ejercicio1()
	return acc/float(n)

def main():
	for n in [10,100,1000,10000]:
		print(' n = ', n , 'E(X) = ', esperanza_ej1(n))


if __name__ == "__main__":
	main()
