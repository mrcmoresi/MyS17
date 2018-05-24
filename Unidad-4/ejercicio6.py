from __future__ import print_function
from random import random
from math import sqrt
from variables import maxVaIndep

## EJERCICIO 6 ##
# F(X) = X^n    0 <= x <= 1
# Generarla con 3 metodos distintos

def metodoDelMaximo(n):
	x = maxVaIndep(n)
	return x

def transformadaInversa(n):
	u = random()
	x = u**(1.0/float(n))
	return x

def aceptacionRechazo(n):
	y = random()
	u = random()
	while u < y**(n-1):
		y = random()
		u = random()

	return y

def esperanzaPorMetodo(N, n):
	#N la cantidad de veces que simulo la variable
	#n parametro de F(x) = X^n

	esp_metodo_1 = 0
	esp_metodo_2 = 0
	esp_metodo_3 = 0
	for _ in range(N):
		esp_metodo_1 += metodoDelMaximo(n)
		esp_metodo_2 += transformadaInversa(n)
		esp_metodo_3 += aceptacionRechazo(n)

	esp_metodo_1 = esp_metodo_1/float(N)
	esp_metodo_2 = esp_metodo_2/float(N)
	esp_metodo_3 = esp_metodo_3/float(N)

	return esp_metodo_1, esp_metodo_2, esp_metodo_3

def main():
	#voy a simular F(x) = X^10
	for N in [10,100,1000,10000]:
		e1, e2, e3 = esperanzaPorMetodo(N, 10)

		print('Metodo del Maximo', 'N ', N, 'E(x)', e1)
		print('Metodo de TI', 'N ', N, 'E(x)', e2)
		print('Metodo de Rechazo', 'N ', N, 'E(x)', e3)
		print('###############################')

if __name__ == "__main__":
	main()