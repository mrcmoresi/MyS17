from __future__ import print_function
from random import random
from variables import poissonNoHomogeneo

def lambda_t(t):
	"""
	Escribo la funcion de lambda del ejercicio
	lambda(t) = 3 + (4 / (t+1))
	"""
	return 3 + (4 / float(t+1))

def main():
	#calculo la esperanza
	#lambda = 7 calculado en el teorico
	# tengo que generar las 10 primeras unidades de tiempo

	I, S = poissonNoHomogeneo(7, lambda_t, 10)
	print(I, S)



if __name__ == "__main__":
	main()
