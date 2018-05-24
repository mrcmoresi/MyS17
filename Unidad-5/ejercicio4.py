from __future__ import print_function
from random import random
from math import exp, log, sqrt

def intervalo(media, desv_std, n):
	"""
	Calcula el intervalo de confianza para una media, desv_std, y un n
	Alfas 
	90%  => 1.64
	95%  => 1.96
	99%  => 2.33
	Tambien se puede calcular como 
	from scipy.stats import norm
	alfa = 0.05
	alfa/2 = 0.025
	norm.ppf(1-alfa/2) 1.96

	"""
	IC = (media - 1.96 * (desv_std / sqrt(n)), media + 1.96 * (desv_std / sqrt(n)))
	return IC


def primerMenor():
	"""
	Funcion que calcula la primer va que cumple Un+1 > Un
	devuleve el n
	"""
	U = random()
	V = random()
	n = 2
	while U <= V:
		n += 1
		U = V
		V = random()
	return n

def simulacion():
	N = 1000
	X = primerMenor()
	media = X
	S_cuadrado = 0
	for n in range(2, N+1):
		X = primerMenor()
		mediaAnt = media
		media += (X - media)/float(n)
		S_cuadrado = (1 - 1/float(n-1)) * S_cuadrado + n*((media - mediaAnt) ** 2)
	desv_std = sqrt(S_cuadrado)
	IC = intervalo(media, desv_std, n)
	return media, S_cuadrado, IC

def main():
	media_muestral, var_muestral, IC = simulacion()
	print("El valor de la media_muestral es {}".format(media_muestral))
	print("El valor de la varianza_muestral es {}".format(var_muestral))
	print("IC con 95% de confianza es {}".format(IC))

if __name__ == "__main__":
	main()
