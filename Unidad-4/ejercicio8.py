from __future__ import print_function
from random import random
from variables import normalPolar, normalEstandaryExponencial

def esperanza_polar(N):
	acc = 0
	for _ in range(N):
		#devuelve dos normales, me quedo con X (eleccion arbitraria)
		x, y = normalPolar()
		acc += x
	return acc/float(N)

def varianza_polar(N):
    """
    Varianza en base a la esperanza con Metodo Polar.
    """
    suma1 = 0
    suma2 = 0
    for _ in range(N):
        x, y = normalPolar()
        suma1 += x # x
        suma2 += x**2 # x**2

    varianza = suma2/float(N) - (suma1/float(N))**2 # V(x) = E(x^2) - E(x)^2

    return varianza



def esperanza_normal_y_exponencial(N):
	acc = 0
	for _ in range(N):
		z, x = normalEstandaryExponencial()
		acc += z

	return acc/float(N)

def varianza_normal_y_exponencial(N):
	suma1 = 0
	suma2 = 0
	for _ in range(N):
		z, x = normalEstandaryExponencial()
		suma1 += z # X
		suma2 += z**2
	varianza = suma2/float(N) - (suma1/float(N))**2
	return varianza


def main():
	print("NORMAL CON EL METODO POLAR")
	for N in [10, 100, 1000, 10000]:
		print('N = ', N, 'E(X) = ', esperanza_polar(N), 'V(X) = ', varianza_polar(N))
	print('\n\n ########################### \n\n')
	print("NORMAL CON EL METODO POLAR")
	for N in [10, 100, 1000, 10000]:
		print('N = ', N, 'E(X) = ', esperanza_normal_y_exponencial(N), 'V(X) = ', varianza_normal_y_exponencial(N))

if __name__ == "__main__":
	main()