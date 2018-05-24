from __future__ import print_function
from random import random, randint
from math import exp, sqrt

def mediaMuestral(muestra):
	"""
	Calcula la media muestral Xbarra = (X1+...+Xn)/n
	"""
	return sum(muestra)/float(len(muestra))

def varianzaMuestral(muestra):
	"""
	calcula la varianza muestral Scuadrado(n) = sumatoria(1, n, (xi - Xbarra(n))^2)/(n-1)
	"""
	media_muestral = mediaMuestral(muestra)
	var = sum([(x - media_muestral)**2 for x in muestra]) / float(len(muestra) - 1)
	
	return var

def bootstrap(muestra, iteraciones):
	exitos = 0
	varianza_sampleo = 0
	media_sampleo = 0
	var = 0
	n = len(muestra)
	media_muestral = mediaMuestral(muestra)
	varianza_muestral = varianzaMuestral(muestra)
	for _ in range(iteraciones):
		#sampleo a partir de los elementos de la muestra
		sampleo = [muestra[randint(0,n-1)] for _ in range(n)]
		#calculo la media a los elementos sampleados
		media_sampleo = sum(sampleo)/n
		varianza_sampleo = 0
		for value in sampleo:
			varianza_sampleo += (value - media_sampleo)**2
		varianza_sampleo /= n-1
		var += (varianza_sampleo - varianza_muestral)**2
	return(var/iteraciones)



def main():
	muestra = [1,3]
	print(bootstrap(muestra, 1000))
	

if __name__ == "__main__":
	main()
