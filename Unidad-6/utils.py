from __future__ import print_function
from random import random
from scipy.stats import chi2

def permutacion(X):
	#Genero permutaciones Equiprobables de un conjunto X
	N = len(X)-1
	for i in range(N,0,-1):
		U = random()
		index = int(i*U)+1
		X[index], X[i] = X[i], X[index]
	return X

def estadistico_ji(k, n, N, p):
	"""
	Calcula el estadistico para el test de Chi^2
	
	T = sum desde j=1 hasta k (Ni - n*pi)^2 /n*pi

	Parametros:
	p : lista de probabilidades p[i] = P(X=i)
	N : frecuencia observada
	k : valores posibles de la muestra, osea cantidad de intervalos
	n : tamanho de la muestra

	"""

	T = 0
	for i in range(k):
		T += (((N[i] - n*p[i]) ** 2) / float((n*p[i])))
	return T


def ji_cuadrado(T, dof):
	"""

	Test de prueba contra Chi^2 (devuelve el p-valor calculado)
	Parametros :
	T : Estadistico de prueba o T observado
	dof : degree of freedom

	"""
	p_valor = 1 - chi2.cdf(T, dof)
	return p_valor


def simulacion(n, it, T, fun_prob, k, p):
	"""
	Aproxima el p-valor a partir de simulaciones

	Parametros:
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

		if estadistico_ji(k, n, Ni, p) >= T:
			exito +=1

	return(exito / it)

def estadistico_D(muestra, F):
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
		D_values.append((j / float(n)) - F(value))
		D_values.append(F(value) - ((j-1) / float(n)))
		j += 1

	return(max(D_values))
		

def test_KS(n, Nsim, d):
	"""
	Funcion que calcula el p-valor mediante el test de KS
	n : tamanho de la muestra
	Nsim : numero de simulaciones
	d : estadistico de KS
	"""
	p_valor = 0
	for _ in range(Nsim):
		uniformes = []
		for j in range(n):
			uniformes.append(random())
		uniformes.sort()
		lst = []
		for j in range(n):
			lst.append((j+1)/n - uniformes[j])
			lst.append(uniformes[j] - (j/float(n)))
		if max(lst) > d:
			p_valor += d

	return (p_valor / Nsim)

def debo_rechazar(p_valor):
	alphas = [0.1, 0.05, 0.01]
	
	for alpha in alphas:
		print("\n Con alpha = {}".format(alpha))
		if p_valor < alpha:
			print("Conclusion: se rechaza H0")
		else:
			print("Conclusion: No hay evidencia suficiente para rechazar H0")
	
