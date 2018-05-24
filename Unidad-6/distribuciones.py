from random import random
from math import log, exp, pi, sqrt, cos, sin

#varianza = sigma **2
#desv_std = sqrt(sigma**2)
### DISCRETAS ####

def uniforme_discreta(n):
	#VA uniforme entre 1 y n
	u = random()
	return int(n*u)+1

def uniforme_discreta_ext(m,k):
	#VA uniforme entre m y k
	u = random()
	return int(u * (k-m+1))+m

def permutacion(X):
	#Genero permutaciones Equiprobables de un conjunto X
	N = len(X)-1
	for i in range(N,0,-1):
		U = random()
		index = int(i*U)+1
		X[index], X[i] = X[i], X[index]
	return X

def subconjunto_aleatorio(r, A):
	#subconjunto aleatorio de r elementos 
	# de un conjunto de A de cardinal N
	N = len(A)-1
	for j in range(N,N-r,-1):
		index = int(j*random())
		A[index], A[j] = A[j], A[index]
	return A[0:r]
	
def geometrica(p):
	#generacion de una va geometrica
	# prob de masa
	# pi = P(X = i) = p* (q**(i-1))
	U = random()
	return int( log(U) / log(1-p) )+1

def bernoulli(p):
	U = random()
	if U<p:
		return 1
	else:
		return 0

def poisson(lamb):
	#genero una VA Poisson con parametro Lamb
	#prob de masa
	#pi = P(X=i) = e**(-lambda) * (lambda**i / i !)
	#E(x) = lambda
	#V(x) = lambda
	U = random()
	i = 0
	p = exp(-lamb)
	F = p
	while(U >= F):
		i += 1
		p = (lamb * p) / float(i)
		F += p
	return i

def Fpoisson(i,lamb):
	#calculo la funcion de  distribucion de una va con distrib de Poisson paramaetro lamb
	p = exp(-lamb)
	F = p
	for _ in range(i):
		p = (p * lamb) / i
		F += p
	return F

def binomial(n, p):
	#generador de va Binomial (n,p) discreta
	# funcion de masa de prob
	#pi = P(X=i) = [n! / (i! * (n-i)!)] * p**i * (1-p)**(n-i)
	U = random()
	i = 0
	c = p / float(1 - p)
	prob = (1 - p)**n
	F = prob
	while(U >= F):
		prob = (c * (n - i) / float(i + 1)) * prob
		F += prob
		i += 1
	return i

def urna(k, vector):
	#metodo de la urna
	#vector es un arreglo con los valores segun el algoritmo
	index = int(random()*k)+1
	return vector[index]
	
#######################
##### CONTINUAS #######
#######################

def maxVaIndep(n):
	#Tengo X1,X2, ..., Xn v.a.i. con funcion de distrib F1,F2,...,Fn
	# X = max{X1, X2, ... , Xn}
	# Fx(a) = F1(a)*...*Fn(a)
	#Fx(x) = x ** n  0<= x <= 1
	uniforms = [random() for _ in range(n)]
	X = max(uniforms)
	return X

def minVaIndep(n):
	#analogo al anterior pero el minimo
	uniforms = [random() for _ in range(n)]
	X = min(uniforms)
	return X

def exponencial(lamb):
	#va continua, con distribucion exponencial de parametro lambda
	# X ~ E(lambda)
	U = random()
	return(-log(U) / float(lamb))

def gamma(n, lamb):
	#generador de va continua con distribucion Gamma(n, lambda)
	U = 1
	for _ in range(n):
		U *= random()
	return -log(U)/lamb

def dosExponenciales(lamb):
	#Generador de dos va X,Y independientes con distribucion exponencial de parametro lambda
	t = 1/lamb * log(random() * random()) #valor de una Gamma(2, lambda)
	U = random()
	X = t * U
	Y = t - X 
	return X, Y

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

def normalPolar():
	#METODO POLAR
	#Simula dos variables Normales estandar
	#transformada de box muller
	U1 = random()
	U2 = random()
	r_cuadrado = -2 * log(U1)
	theta = 2 * pi * U2
	X = sqrt(r_cuadrado) * cos(theta)
	Y = sqrt(r_cuadrado) * sin(theta)
	return X,Y

def dosNormales():
	#MEJORA DEL METODO POLAR
	#genera dos normales estandar mu = 0 sigma = 1
	#una mejora es evitar el calculo de las funciones trigonometricas
	#generar un punto aleatorio en el circulo unitario
	
	while True:
		V1, V2 = random(), random()
		if V1 ** 2 + V2 ** 2 <= 1:
			break
	S = V1 ** 2 + V2 ** 2
	C = sqrt(-2 * log(S) / S)
	X = V1 * C
	Y = V2 * C
	return X, Y

def normalEstandaryExponencial():
    """
    Ejemplo 5f libro de simulacion de S.M Ross
    Genera una v.a. Z con distribucion Normal Estandar ==> Z ~ N(0, 1)
    Genera una v.a. X con distribucion Exponencial ==> X ~ Exp(1).
    """
    y1 = exponencial(1)
    y2 = exponencial(1)
    while y2 - ((y1 - 1)**2/2.0) <= 0:
        y1 = exponencial(1)
        y2 = exponencial(1)

    x = y2 - ((y1 - 1)**2/2.0)
    u = random()

    if u < 0.5:
        z = y1
    else:
        z = -y1

    return z, x

def procesoDePoisson(T, lamb):
	#genero los eventos hasta el tiempo T, con intensidad Lambda
	# devuelvo la cantidad de eventos ocurridos I, y los tiempos S (arreglo)
	#Proceso de poisson homogeneo
	t = 0 # tiempo transcurrido
	I = 0 # Numero de evento
	S = [] # S[1], S[2] ... => tiempo de eventos
	while True:
		U = random()
		if t-log(U) / lamb > T:
			break
		else:
			t = t -log(U) / lamb
			I += 1
			S.append(t)
	return I, S

def poissonNoHomogeneo(lamb, fun_lambda, tiempo):
	#Generacion de eventos en el intervalo usando el Algoritmo de Adelgazamiento
	# para el proceso de Poisson no Homogeneo.
	# devuelve el numero de eventos y el arreglo correspondiente
	t = 0
	i = 0 #numero de eventos
	S = [] # S[1], S[2] ===> tiempos de eventos
	while True:
		U = random()
		if t - (log(U) / float(lamb)) > tiempo:
			break
		else:
			t -= log(U)/float(lamb)
			v = random()
			if v < (fun_lambda(t)/float(lamb)):
				i += 1
				S.append(t)
	return i, S


def poissonNoHomogenenoMejorado(lambdas, intervalos, fun_lamb, T):
	#Generador de proceso de poisson no homogeneo con la mejora adelgazamiento en la seleccion del lambda
	#IDEA: elegir un lambda particular para cada intervalo, de modo que se ajuste lo mas posible a la funcion de distrib.

	t = 0 #Acumula tiempos
	i = 0 #Acumula cantidad de arribos
	S = []
	J = 1 # Recorre intervalos
	
	while True:
		U = random()
		X = -log(U)/lambdas[J]

		while t + X > intervalos[J]:
			if J == k+1:
				break
			else:
				X = (X - intervalos[J] + t) * lambdas[J] / lambdas[J+1]
				t = intervalos[J]
				J += 1
		t = t + X
		V = random()
		if V < fun_lamb(t) / float(lamb):
			i += 1
			S.append(t)
	return S

def main():
	
	print(procesoDePoisson(8, 4))


if __name__ == "__main__":
	main()
