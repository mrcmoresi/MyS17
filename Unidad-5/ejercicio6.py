from __future__ import print_function
from random import random, randint
from math import exp, sqrt

def bootstrap(N, n, a, b, muestra):
	"""
	Parametros para el metodo de bootstrap
	En este caso se esta utilizando para aproximar el valor de p
	N : cantidad de iteraciones
	n : tamanho de la muestra
	a,b : condiciones del enunciado
	muestra : valores de la muestra
	"""
	exitos = 0

	#calculo la media muestral
	media_muestral = sum(muestra)/len(muestra)
	for _ in range(N):
		#sampleo aleatoriamente n elementos de la muestra (en este caso 10)
		sampleo = [muestra[randint(0,9)] for _ in range(n)]
		#tengo las "generadas" por bootstrap en sampleo
		# construyo Y ~ sampleadas/n
		# si a < Y - media_muestral < b => exito
		y = sum(sampleo)/len(sampleo)
		if a < y-media_muestral and y-media_muestral < b:
			exitos += 1
	
	return exitos/float(N)


def main():
	"""
	Sean X1,...,Xn variables aleatorias independientes e identicamente distribuias con media mu desconocida. Para a y b constantes dadas,
	a < b, nos interesa estimar p = P (a < sum desde i=1 hasta n ((Xi / n)- mu) <b)
	-Estimar p asumiendo que para n=10, los valores de las variables Xi 
	resultan 56, 101, 78, 67, 93, 87,64, 72, 80 y 69. 
	Sean a = - 5 y b = 5.
	"""
	muestra = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
	a = -5
	b = 5
	n = len(muestra)

	for N in [10, 100, 1000, 10000, 100000]:
		print("N = ", N, "||  p = ", bootstrap(N, n, a, b, muestra))
	

if __name__ == "__main__":
	main()
