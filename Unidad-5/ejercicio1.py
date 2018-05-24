from __future__ import print_function
from distribuciones import normal
from random import random
from math import sqrt

def simulacion(iteraciones):
	# n : cantidad de iteraciones

	#genero X ~ N(0,1)
	X = normal(0,1)
	
	#Contador de simulaciones realizadas
	N = iteraciones
	#el primer valor de la media va a ser el primer valor de la normal generada
	media = X
	#Varianza Muestral (Valor inicial S_cuadrado(1) = 0)
	S_cuadrado = 0
	#genero los 30 valores de la Normal y calculo la Media y Varianza Muestral
	for n in range(2, N+1):
		X = normal(0,1)
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - (1 / (float(n) - 1))) * S_cuadrado + n * ((media - mediaAnt) ** 2)
	
	#tomando los resultados de las primeras 30 simulaciones
	#vamos a iterar hasta que la desviacion standar del estimador = sqrt(var/j) > d
	while sqrt(S_cuadrado / float(n)) > 0.1:
		N += 1
		n += 1
		X = normal(0,1)
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - 1 / (float(n) - 1)) * S_cuadrado + n * ((media - mediaAnt) ** 2)

	#Devuelvo la media_muestra, varianza_muestral y la cantidad de simulaciones que necesite para cumplir la condicion
	return media, S_cuadrado, N 


def main():
	"""
	Generar n valores de una variable aleatoria normal estandar de manera tal que se cumplan las condiciones: 
	n >= 30 y S /sqrt(n) <0.1, siendo S la desviacion estandar muestral de los n datos generados.
	"""
	N = 30
	media_muestral, var_muestral, n = simulacion(N)
	print("El valor de la media_muestral es {}".format(media_muestral))
	print("El valor de la varianza_muestral es {}".format(var_muestral))
	print("Necesite {} cantidad de simulaciones para cumplir que S/sqrt(n) < 0.1".format(n))


if __name__ == "__main__":
	main()
