from __future__ import print_function, unicode_literals
from random import random
from math import sqrt

def vaMinima():
	#calcula el minimo{n : sum desde i=1 hasta n Ui > 1}
	N = 0
	acc = 0.0
	#si acc <= 1 entonces sumo una uniforme mas
	while acc <= 1.0:
		acc += random()
		N += 1
	return N

def simulacion():
	N = 1000
	X = vaMinima()
	media = X
	S_cuadrado = 0
	for n in range(2, N+1):
		X = vaMinima()
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - 1 / (float(n) - 1 )) * S_cuadrado + n * ((media - mediaAnt) ** 2)
	
	S = sqrt(S_cuadrado)
	
	IC = (media - 1.96*(S / sqrt(n)), media + 1.96*(S / sqrt(n)))

	return media, S_cuadrado, S, IC
	

def main():
	"""
	Para U1,U2,... variables aleatorias uniformemente distribuidas en el intervalo(0,1), se define:
	N=Minimo{n:sum i=1 to n Ui>1} Es decir, N es igual a la cantidad de numeros aleatorios que deben sumarse para exceder a 1.
	Como se mostro en el Problema 3 de la Guia N3,E[N] =e.Calcular la varianza del estimador N correspondiente a 1000 ejecuciones de la simulacion y dar un
	a estimacion dee mediante un intervalo de confianza de 95%.
	"""
	media, S_cuadrado, S, IC = simulacion()
	print("Media Muestral = ", media)
	print("Varianza Muestral = ", S_cuadrado)
	print("Desviacion Estandar Muestral (sigma) = ", S)
	print("Intervalo de confianza = ", IC)

if __name__ == "__main__":
	main()
