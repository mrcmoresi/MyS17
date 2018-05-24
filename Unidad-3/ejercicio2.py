from __future__ import print_function
from random import random
from math import exp

def exacto():
	s = 0
	for k in range(1, 10001):
		s += exp(k/10000)
	return s

def ejercicio2(n):
	N = 10000
	s = 0
	for _ in range(n):
		U = random()
		k = int(U * 10000)+1
		s += exp(k/float(N))
	#promedio la salida
	return (N*s)/float(n)

def main():
	print("el valor exacto es = ", exacto())
	for n in [10, 100, 1000, 10000]:
		aprox = ejercicio2(n)
		print("n = ", n, " || valor aproximado = ", aprox)

if __name__ == "__main__":
    main()
