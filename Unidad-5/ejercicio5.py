from __future__ import print_function
from random import random
from math import sqrt
"""
Estimador por intervalo de una proporcion
En el caso de una Bernoulli el estimador por intervalo del parametro p tambien es el estimador por
intervalo de la media poblacional
el estimador para la varianza
Xi =[muestra de valores bernoulli (0,1)]
x_barra = sum(Xi)/len(Xi)
var_barra = x_barra *(1-x_barra)

IC de una proporcion
(x_barra - Zalpha/2 * ((sqrt(x_barra *(1-x_barra))/) / sqrt(n)) , x_barra + Zalpha/2 * ((sqrt(x_barra *(1-x_barra))/) / sqrt(n)))
"""

def intervalo(media, desv_std, n):
	"""
	Calcula el intervalo de confianza para una media, desv_std, y un n
	Alfas 
	90%  => 1.64
	95%  => 1.96
	99%  => 2.33
	Tambien se puede calcular como 
	from scipy.stats import norm
	alfa = 0.05
	alfa/2 = 0.025
	norm.ppf(1-alfa/2) 1.96

	"""
	IC = (media - 1.96 * (desv_std / sqrt(n)), media + 1.96 * (desv_std / sqrt(n)))
	return IC

def generarPI():
    PI = 0
    U = random() # U ~ U(0, 1)
    V = random() # V ~ U(0, 1)
    X = 2*U - 1 # X ~ U(-1, 1)
    Y = 2*V - 1 # Y ~ U(-1, 1)

    # Punto cae adentro del circulo de radio 1
    if X**2 + Y**2 <= 1:
        PI += 1
    
    PI = 4 * PI # Puede ser 0 o 4

    return PI

def simulacion(iteraciones):
	# n : cantidad de iteraciones

	#genero X ~ N(0,1)
	X = generarPI()
	
	#Contador de simulaciones realizadas
	N = iteraciones
	#el primer valor de la media va a ser el primer valor de la normal generada
	media = X
	#Varianza Muestral (Valor inicial S_cuadrado(1) = 0)
	S_cuadrado = 0
	#genero los 30 valores de la Normal y calculo la Media y Varianza Muestral
	for n in range(2, iteraciones+1):
		X = generarPI()
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - (1 / (float(n) - 1))) * S_cuadrado + n * ((media - mediaAnt) ** 2)
	
	#tomando los resultados de las primeras 30 simulaciones
	#vamos a iterar hasta que la longitud del intervalo sea menor que 0.1
	while 2*1.96*sqrt(S_cuadrado / float(n)) > 0.1:
		N += 1
		n += 1
		X = generarPI()
		mediaAnt = media
		media += (X - media) / float(n)
		S_cuadrado = (1 - 1 / (float(n) - 1)) * S_cuadrado + n * ((media - mediaAnt) ** 2)

	#construyo el intervalo con la media calculada, la desviacion standard y el n, en este caso se llama j pero representa la cantidad de elementos que genere 
	IC = intervalo(media, sqrt(S_cuadrado),n)

	#calculo la longitud del intervalo resultante  con 95% de confianza
	# 2 * Zalpha/2 * desv_standar / n
	longitud =2*1.96*sqrt(S_cuadrado / float(n))
	#media_muestra, varianza_muestra, cantidad de  iteraciones, longitud del intervalo, IC
	return media, S_cuadrado, N, longitud, IC

def main():
	media_muestral, var_muestral, N, longitud, IC = simulacion(10)
	print("El valor de la media_muestral es {}".format(media_muestral))
	print("El valor de la varianza_muestral es {}".format(var_muestral))
	print("IC con 95% de confianza es {}".format(IC))
	print("Cantidad de iteraciones {}".format(N))
	print("Longitud del intervalo {}".format(longitud))


if __name__ == "__main__":
	main()