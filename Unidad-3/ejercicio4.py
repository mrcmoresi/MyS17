from __future__ import print_function
from random import random
from math import exp, factorial

def poisson(lamb):
	#V.A con distribucion de Poisson con parametro Lambda
	#lamb => parametro lambda
	U = random()
	i = 0
	#p0 = e**(-lamb)
	p = exp(-lamb)
	F = p
	while U >= F:
		#pi=(p(i-1)*lambda) / i+1
		p = (p * lamb)/float(i+1)
		F += p
		i += 1
	return i

def transformadaInversa(k,lamb):
	pj = 0
	j = 0
	#calculo la sumatoria del divisor
	while j <= k:
		pj += (lamb**j / float(factorial(j)))
		j += 1
	sum_pj = pj
	#genero la va con distribucion de Poisson(lamb)
	u = random()
	i = 0
	#construyo el numerador
	p_i = 1/float(sum_pj)
	f = p_i
	while u >= f:
		p_i = (lamb * p_i) / float(i+1)
		f += p_i
		i += 1
	return i


def aceptacionYrechazo(k, lamb):
	x = poisson(lamb)
	while x >= k:
		x = poisson(lamb)
	return x


def esperanzaTI(k, lamb, n):
	acc = 0
	for _ in range(n):
		acc += transformadaInversa(k, lamb)
	return acc/float(n)

def esperanzaAyR(k, lamb, n):
	acc = 0
	for _ in range(n):
		acc += aceptacionYrechazo(k, lamb)
	return acc/float(n)

def main():
	for n in [100,1000]:
		print("Aceptacion y rechazo")
		print("n=", n, "E(X)=", esperanzaAyR(10,2,n))
	print('#######################')
	for n in [100,1000]:
		print('Transformada Inversa')
		print('n=', n, 'E(X)=', esperanzaTI(10,2,n))

if __name__ == "__main__":
	main()



