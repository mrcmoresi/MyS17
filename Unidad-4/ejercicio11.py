from __future__ import print_function
from random import random
from variables import procesoDePoisson, uniforme_discreta_ext

def main():
	# T = 1 hora
	# lambda = 5 por hora
	I, S = procesoDePoisson(1,5)
	print('Cantidad de colectivos que arribaron = ', I)
	print('\n \n Tiempos en los que arribaron = ', S)
	publico = 0 
	for _ in range(I):
		#Cantidad de personas por colectivo
		publico += uniforme_discreta_ext(20,40)
	print('\n \n Publico que asiste', publico)

if __name__ == "__main__":
	main()
