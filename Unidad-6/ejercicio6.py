from __future__ import print_function, division
from utils import *
from math import exp
from distribuciones import exponencial

def F():
	return exponencial(1)

def F_e(x):
	F_e = 1 - exp(-x)
	return F_e

def main():
	"""
	Generar los valores correspondientes a 10 variables aleatorias exponenciales independientes,
	cada  una  con  media  1.   Luego,  en  base  al  estadistico  de  prueba  de  Kolmogorov-Smirnov,
	aproxime  el p valor de la prueba de que los datos realmente provienen de una distribucion 
	exponencial con media 1
	"""
	Yi = []
	n = 10
	for _ in range(n):
		Yi.append(F())
	Yi.sort()
	#print(Yi)
	Nsim = 1000
	D = estadistico_D(Yi, F_e)
	p_value = test_KS(n, Nsim, D)
	print("El estadistico tiene un valor de {}".format(D))
	print("El p-valor obtenido por el test de KS es {}".format(p_value))
	debo_rechazar(p_value)
	

if __name__ == "__main__":
	main()
