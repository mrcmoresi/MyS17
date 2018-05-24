from __future__ import print_function, division
from utils import *
from math import exp

def F(x, lamb):
	F = 1 - exp(-x * lamb)
	return F


def estadistico_D(muestra, F, lamb):
	"""
	Calculo del estadistico para el test de KS
	muestra : lista con los elementos observados
	F : funcion contra la cual comparo la muestra
	salida calcula
	D = max 1<= j <= n { (j/n) - F(Y(j)), F(Y(j)) - (j-1)/n}
	"""
	j = 1
	D_values = []
	n = len(muestra)
	for value in muestra:
		D_values.append((j / float(n)) - F(value, lamb))
		D_values.append(F(value, lamb) - ((j-1) / float(n)))
		j += 1

	return(max(D_values))

def main():
	"""
	En  un  estudio  de  vibraciones,  una  muestra  aleatoria  de  15  componentes  del  avion  fueron
	sometidos a fuertes vibraciones hasta que se evidenciaron fallas estructurales.  Los datos proporcionados
	son los minutos transcurridos hasta que se evidenciaron dichas fallas.
	1.6 10.3 3.5 13.5 18.4 7.7 24.3 10.7 8.4 4.9 7.9 12 16.2 6.8 14.7
	Pruebe la hipotesis nula de que estas observaciones pueden ser consideradas como una muestra de la
	poblacion exponencial.

	"""
	Nsim = 1000
	Yi = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
	Yi.sort()
	n = len(Yi)
	#X_barra  estimador insesgado de la media de la va exponencial
	X_barra = sum(Yi)/float(len(Yi))
	
	print("X barra {}".format(X_barra))
	#X_barra = 1/ Lambda_barra => lambda_barra = 1 / X_barra
	lamb_barra = 1/float(X_barra)
	print("lambda barra {}".format(lamb_barra))

	D = estadistico_D(Yi, F, lamb_barra)
	p_value = test_KS(n, Nsim, D)

	print("El valor del estadistico es {}".format(D))
	print("El p-valor obtenido es {}".format(p_value))
	debo_rechazar(p_value)
	
if __name__ == "__main__":
	main()

