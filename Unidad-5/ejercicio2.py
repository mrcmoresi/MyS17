from __future__ import print_function
from random import random
from math import exp, sqrt

def integral():
	y = random()
	X = exp(y ** 2)
	return X

def monteCarlo(N):
	acc = 0.0
	for i in range(N):
		acc += integral()
	return acc/N

def simulacion():
	#simulaciones realizadas
	N = 100 #minimo numero de simulaciones
	X = integral() #Genero un valor de la integral
	media = X #media muestral (valor inicial = X1)
	S_cuadrado = 0
	for n in range(2, N+1):
		X = integral()
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - 1 / (float(n) -1 )) * S_cuadrado + n * ((media - mediaAnt) ** 2)
	
	while sqrt(S_cuadrado / float(n)) > 0.01:
		N += 1
		n += 1
		X = integral()
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - 1 / (float(n) - 1)) * S_cuadrado + n * ((media - mediaAnt) ** 2)
	S = sqrt(S_cuadrado)
	return media, S, N


def main():
	
	"""
	Estimar mediante el metodo de Monte Carlo la integral
	0 1 integral exp(x2)dx.Generar al menos 100 valores y detenerse cuando la desviacion estandar del estimador sea menor que 0.01
	"""
	media, S, N = simulacion()
	print("Media Muestral = ", media)
	print("Desviacion Estandar Muestral = ", S)
	print("cantidad de iteraciones = ", N)


if __name__ == "__main__":
	main()
