# -*- coding: utf-8 -*-
from __future__ import print_function, division
from distribuciones import *
from scipy.special import ndtr
from math import sqrt

"""
Problema de las dos muestras
H0; las n+m variables X1...Xn Y1...Ym son independientes y provienen de una distrib F
Rango  = sum from i=1 to n R(Xi)
R(Xi) es la posicion que ocupa el elemento Xi luego del ordenamiento
p-valor = 2*min{PHo(R>=2),PHo(R<=2)}

"""


def permutacion(X):
	#Genero permutaciones Equiprobables de un conjunto X
	N = len(X)-1
	for i in range(N,0,-1):
		U = random()
		index = int(i*U)+1
		X[index], X[i] = X[i], X[index]
	return X

def rango(muestra_1, muestras):
	"""
	calula el rango de la muestra_1 en muestras en caso de repeticion toma el promedio
	muestra_1 : muestra de tamanho n
	muestras : muestra n+m
	"""
	muestras.sort()

	muestraCopia = list(muestra_1)
	muestraCopia.sort()

	R = []
	j = 0
	while len(muestraCopia) != 0:
		valor = muestraCopia[0]
		#cuento la cantidad de ocurrencias del 1er valor de la muestra
		cantValor = muestraCopia.count(valor)
		s = 0
		#voy a calcular el promedio de veces que aparece ese elemento en la muestra
		for j in range(cantValor):
			#cuento las posiciones en las que aparece
			for i in range(muestras.count(valor)):
				s += muestras.index(valor) + (i + 1)
			muestraCopia.pop(0)
		#tomo el promedio
		s = s / float(muestras.count(valor))
		R.append(s)

	return sum(R)


def rangos_pequenos(n, m, r):
	"""
	n : tamanho de la muestra que nos interesa
	m : tamanho de la segunda muestra
	r : observado
	"""
	if n == 1 and m == 0:
		if r  <= 0:
			return(0)
		else:
			return(1)
	elif n == 0 and m == 1:
		if r < 0:
			return(0)
		else:
			return(1)
	else:
		if n == 0:
			return rangos_pequenos(0, m-1, r)
		elif m == 0:
			return rangos_pequenos(n-1, 0, r-n)
		else:
			value_1 = n/float(n+m)*rangos_pequenos(n-1,m,r-n-m)
			value_2 = m/float(n+m) * rangos_pequenos(m, m-1, r)
			return (value_1 + value_2) 




def p_valor_exacto(n, m, r):
	"""
	n : tamanho de la muestra que nos interesa
	m : tamanho de la segunda muestra
	r : observado
	Test de suma de rangos para n y m pequenhos
	Pn,m(r) = P(R<= r)
	p_value = 2 * min {Ph0(R>=r), Ph0(R<=r)}
	"""
	return (2 * min(rangos_pequenos(n,m,r), 1 - rangos_pequenos(n,m,r-1)))




def aprox_por_normal(n, m, r):
	"""
	test de rango para n y m grandes
	Aproximo el p_valor por una normal standard
	n : tamanho de la muestra mas chica
	m : tamanho de la muestra mas grande
	r : rango observado
	"""
	#esperanza de Ri
	#esperanza_ri = (n+m+1) / 2 

	#Esperanza de R
	esperanza_R = n * ((n+m+1) / 2.0 )
	#Varianza de R
	varianza_R = (n*m)*((n+m+1) / 12.0)

	#Normalizo a una N(0,1)
	Z = (r - esperanza_R) / sqrt(varianza_R)

	if r <= esperanza_R:
		p_value = 2 * ndtr(Z)
	else:
		p_value = 2 * (1 - ndtr(Z))

	return p_value




def simulacion_p_valor(muestra_1, muestra, r, iteraciones):
	"""
	simulo el p_valor
	muestra_1 : muestra de interes
	muestra : n + m muestra
	r : rango observado
	it : cantidad de simulaciones
	Si los n+m datos son todos distintos entonces las permutaciones son equiprobables
	por lo tanto teniendo el r observado se puede determinar el p-valor simulando N permutaciones
	de los primeros n+m numeros naturales y calculando el Rango a cada permutacion
	"""
	n = len(muestra_1)
	
	R_max = 0
	R_min = 0

	for _ in range(iteraciones):
		muestra_shuffle = permutacion(muestra)
		sub_muestra = muestra_shuffle[0:n]

		R = rango(sub_muestra, muestra)

		if R >= r:
			R_max += 1
		if R < r:
			R_min += 1

		p_value = 2 * min(R_max / float(iteraciones), R_min / float(iteraciones))

	return p_value



def main():
	"""
	Un experimento disenhado para comparar dos tratamientos contra la corrosion arrojo los sigu-
	ientes datos (los cuales representan la maxima profundidad de los agujeros en unidades de milesima de
	pulgada) en pedazos de alambre sujetos a cada uno de los tratamientos por separado:
	Tratamiento 1:	65.2    67.1    69.4    78.4    74.0    80.3
	Tratamiento 2:	59.4    72.1    68.0    66.2    58.5
	
	a)  Calcular el	p−valor exacto de este conjunto de datos, 
	correspondiente a la hipotesis de que ambos	tratamientos tienen resultados identicos.
	b) Calcular el	p−valor aproximado en base a una aproximacion normal,
	c) Calcular el p−valor aproximado en base a una 
	"""
	muestra_1 = [65.2, 67.1, 69.4, 78.4, 74.0, 80.3]
	muestra_2 = [59.4, 72.1, 68.0, 66.2, 58.5]

	#Me aseguro que la primera sea la de menor tamanaho
	if len(muestra_1) > len(muestra_2):
		temp = muestra_1
		muestra_1 = muestra_2
		muestra_2 = temp
	
	n = len(muestra_1)
	m = len(muestra_2)

	iteraciones = 1000
	print("Rango de la muestra 1 {}".format(rango(muestra_1, muestra_1+muestra_2)))
	print("Rango de la muestra 2 {}".format(rango(muestra_2, muestra_1+muestra_2)))
	#Calculo exacto del rango de las muestras
	r = rango(muestra_1, muestra_1+muestra_2)
	#inciso a
	#calculo el p_valor exacto 
	# p_value = 2 * min {Ph0(R>=r), Ph0(R<=r)}
	
	p_value = p_valor_exacto(n,m,r)
	print("El valor exacto del p_valor es {}".format(p_value))

	#inciso b
	#aproximar el p_valor em base a una aproximacion normal
	p_value_aprox = aprox_por_normal(n,m,r)
	print("El valor aproximado del p_valor es {}".format(p_value_aprox))

	#inciso c
	#simular el p_valor
	p_value_sim = simulacion_p_valor(muestra_1, muestra_1+muestra_2, r, iteraciones)
	print("El valor simulado del p_valor es {}".format(p_value_sim))	
	
	


if __name__ == "__main__":
	main()
