from __future__ import print_function, division
from random import random
from scipy.stats import chi2
from scipy.special import chdtrc

"""
Prueba de bondad de ajuste

Test ji_cuadrado y simulacion para conseguir el p_valor 
- Ejercicio 1 y 2

Test Kolmogorov - Smirnov  Con parametros determinados
- Ejercicio 2, 3 y 4

Test Kolmogorov - Smirnov  SIN parametros determinados
- Ejercicio 5 y 8 (8 es mas completo)

Problema de las dos muestras
- Ejercicio 9 y 10

Validacion de Poisson y Test de Kruskall Wallis para multiples muestras
- poission.py
"""


def estadistico(k, n, N, p):
	"""""
	calculo del estadistico

	p : lista de probabilidades p[i] = P(X=i)
	N : frecuencia observada
	k : valores posibles de la muestra, osea cantidad de intervalos
	n : tamanho de la muestra
	"""""
	T = 0
	for i in range(k):
		T += (((N[i] - (n*p[i])) **2 ) /float(n*p[i]))
	return T

def ji_cuadrado(T, dof):
	"""
	T estadistico de prueba o T observado
	dof degree of fredoom
	"""
	p_valor = 1 - chi2.cdf(T, dof)

	return p_valor

def fun_prob():
	U = random()
	if U < 1/2:
		return(2)
	elif U <= 3/4:
		return(1)
	else:
		return(3)


def simulacion(n, it, T, fun_prob, k, p):
	"""
	parametros de entrada
	it : cantidad de simulaciones
	T : estadistico de prueba t observado
	fun_prob : funcion de probabilidad que se va a usar
	n : tamanho de la muestra
	k : valores posibles de la muestra, cantidad de intervalos
	p : lista de probabilidades p[i] = P(X=i)
	"""
	exito = 0
	for _ in range(it):
		#calculo n valores de la funcion de prob
		distribucion = [fun_prob() for _ in range(n)]
		#calculo la frecuencia para valor posible (en este caso roja, blanca o rosa) 
		Ni = [distribucion.count(i+1) for i in range(k)]
	
	#calculo el estadistico para cada muestra si da menor que el estadistico original T cuento un exito
		if estadistico(k, n, Ni, p) >= T:
			exito +=1


	return (exito / float(it))


def main():
	"""
	De acuerdo con la teoria genetica de Mendel, cierta planta de guisantes debe producir flores blancas, rosas o rojas
	con probabilidad 1/4, 1/2 y 1/4, respectivamente. Para verificar experimentalmente la teoria,
	se estudio una muestra de 564 guisantes, donde se encontro que 141 produjeron flores blancas,
	291 flores rosas y 132 flores rojas
	Para aproximar por chi cuadrado
	1 - obtener el estadistico
	2 - ejecutar ji_cuadrado con el estadistico obtenido y los dof igual a la cantidad de histogramas -1

	Para simulacion
	1 - usamos el mismo estadistico
	2 - en este caso que solo nos interesa ver que proviene de una F, llamamos a simulacion con ciertos parametros
	"""

	it = 10000
	pi = [1/4, 1/2, 1/4]
	Ni = [141, 291, 132]
	k = len(pi)
	dof = k-1
	n = sum(Ni)
	T = estadistico(k, n, Ni, pi)
	sim = simulacion(n, it, T, fun_prob, k, pi)
	#Aproximacion chi cuadrado
	print("Estadistico igual a {}".format(T))
	print("El p-valor(Chi cuadrado) es igual a {}".format(ji_cuadrado(T, dof)))
	#simulado
	print("Simulacion el p-valor es igual a {}".format(sim))

if __name__ == "__main__":
	main()
