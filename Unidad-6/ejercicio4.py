from __future__ import print_function, division
from distribuciones import exponencial
from utils import estadistico_D, test_KS, debo_rechazar
from math import exp

def F(x):
	"""
	Distribucion exponencial con media 50
	distrib exponencial de parametro lamba
	cdf (cumulative distribution function)
	F = (1 - exp(-lambda * x))
	media = 1 / lambda
	"""
	F = (1 - exp(-x / 50))
	return F


def main():
	"""
	Calcular una aproximación del p − valor de la hipótesis:
	“Los siguientes 13 valores provienen de una distribución exponencial con media 50”:
	86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99.

	Metodo de Ks para Va continuas, quiero ver que cierta muestra sigue una distribucion F con parametro conocido
	1 - calcular el estadistico, el cual tiene como parametros el conjunto de datos y la F que es el funcion de distribucion con la cual quiero comparar
	por ejemplo si es exponencial F = (1 - exp(-lambda * x)) (cdf de scipy)
	2 - usando el estimador obtenido previamente puedo hacer las simulaciones con el test_KS, pasandole el tamanho de la muestra, cant de simulaciones y el estadistico obtenido
	3 - obtengo el p-valor
	"""

	Yi = [86, 133, 75, 22, 11, 144, 78, 122, 8, 146, 33, 41, 99]
	Yi.sort()

	n = len(Yi)
	Nsim = 1000

	D = estadistico_D(Yi, F)
	p_value = test_KS(n, Nsim, D)

	print("El estadistico tiene un valor de {}".format(D))
	print("El p-valor obtenido por el test de KS es {}".format(p_value))
	debo_rechazar(p_value)


if __name__ == "__main__":
	main()
