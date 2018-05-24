from __future__ import print_function, division
from math import sqrt, log

from scipy.special import ndtr
from scipy.stats import norm
from random import random
"""
# Exponecial: lambda = 1/X-barra
# --------------------------------
# Normal: Mirar Ejercicio 08
# --------------------------------
# Binomial(t, p desconocido): p = X-barra/t
# --------------------------------
# Bernoulli: caso Binomial(1, p desconocido) --> probabilidad = p --> Rango = {0,1}
# --------------------------------
# Geometrica: p = 1/X-barra
# --------------------------------
# Poisson: lambda = X-barra --> mirar ejemplos.py
# --------------------------------
"""

def debo_rechazar(p_valor):
	alphas = [0.1, 0.05, 0.01]
	
	for alpha in alphas:
		print("\n Con alpha = {}".format(alpha))
		if p_valor < alpha:
			print("Conclusion: se rechaza H0")
		else:
			print("Conclusion: No hay evidencia suficiente para rechazar H0")

def normal(mu, sigma):
	# Generacion de va continua con distrib Normal con parametro mu y sigma
	Z = 0
	while True:
		#simulo dos uniformes (0,1)
		U = random()
		V = random()
		# simulo dos exponenciales de parametro lambda = 1
		Y1 = -log(U)
		Y2 = -log(V)

		if Y2 >= (Y1 - 1) ** 2 / 2:
			break
	if random() < 0.5:
		Z = Y1 * sigma + mu
	else:
		Z = -Y1 * sigma + mu

	return Z


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
	S_cuadrado = sum([(x - media_muestral)**2 for x in muestra]) / float(len(muestra) - 1)

	return S_cuadrado

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


def pValor_simulado(Nsim, n, d, args):
	"""
	Nsim : cantidad de simulaciones
	n : tamanho de la muestra
	d : valor observado (estadistico D)
	args : argumentos para la funcion
	"""

	Xi = []
	exitos = 0
	uniformes = []
	D_sim_values = []
	for _ in range(Nsim):
		#simulo muestra de tamanho n que siguen una distri normal con los parametros previamente estimados
		#args[0] media muestral estimada
		#args[1] varianza muestral estimada
		#normal() metodo descripto en el teorico para generar una va con distrib normal
		Xi = [normal(args[0], args[1]) for _ in range(n)]
		Xi.sort()
		media_barra = mediaMuestral(Xi)
		sigma_barra = sqrt(varianzaMuestral(Xi))
		j = 1
		for value in Xi:
			D_sim_values.append((j/float(n)) - norm.cdf(value, loc=media_barra, scale=sigma_barra))
			D_sim_values.append(norm.cdf(value, loc=media_barra, scale=sigma_barra) - (j-1 / float(n)))
			j += 1
		D_sim = max(D_sim_values)

		if D_sim > d:
			exitos += 1
		D_sim_values = []
		Xi = []
	p_valor_estimado = (exitos / float(Nsim))

	return p_valor_estimado


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


def main():
	"""
	Decidir si los siguientes datos corresponden a una distribucion Normal:
	91.9 97.8 111.4 122.3 105.4 95.0 103.8 99.6 96.6 119.3 104.8 101.7.
	Calcular una aproximacion del p-valor.
	"""
	Yi = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
	Yi.sort()

	n = len(Yi)
	Nsim = 1000
	sigma_barra = sqrt(varianzaMuestral(Yi))
	x_barra = mediaMuestral(Yi)
	
	#calculo el estadistico de KS
	j = 1
	D_values = []
	for value in Yi:
		D_values.append((j / float(n)) - ndtr((value - x_barra)/float(sigma_barra)))
		D_values.append(ndtr((value - x_barra)/float(sigma_barra))-(j-1)/float(n))
		j += 1
	estadistico_D = max(D_values)
	
	p_value = test_KS(n, Nsim, estadistico_D)
	print("El estadistico tiene un valor de {}".format(estadistico_D))
	print("El p_valor obtenido es {}".format(p_value))
	debo_rechazar(p_value)
	#como el p_valor esta muy cerca de los umbrales de rechazo voy a simular muestras para ver si puedo obtener mas informacion
	#para saber si rechazar o no

	p_valor_simulado = pValor_simulado(Nsim, n, estadistico_D, [x_barra, sigma_barra])
	print("\n \n Simulo el p valor \n")
	print("P - valor simulado {}".format(p_valor_simulado))
	debo_rechazar(p_valor_simulado)



if __name__ == "__main__":
	main()
