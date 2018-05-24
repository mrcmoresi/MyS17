from __future__ import print_function, division
from random import random
from utils import ji_cuadrado, simulacion, estadistico_ji
 
def fun_dado():
	"""
	Distribucion de tirar un dado honesto
	"""
	U = random()
	if U < 1/6:
		return(1)
	elif U <= 2/6:
		return(2)
	elif U <= 3/6:
		return(3)
	elif U <= 4/6:
		return(4)
	elif U <= 5/6:
		return(5)
	else:
		return(6)

def main():
	"""
	Para verificar que cierto dado no estaba trucado, se registraron 1000 lanzamientos, 
	resultando que el número de veces que el dado arrojó el valor i(i=1,2,3,4,5,6) fue, 
	respectivamente, 158, 172, 164,181, 160, 165. Aproximar el p−valor de la prueba: “el dado es honesto”
	"""

	pi = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
	Ni = [158, 172, 164, 181, 160, 165]
	n = sum(Ni)
	k = len(pi)
	dof = k-1
	it = 1000
	T = estadistico_ji(k, n, Ni, pi)
	chi2 = ji_cuadrado(T, dof)

	sim = simulacion(n, it, T, fun_dado, k, pi)
	print("El valor del estadistico observado T es {}".format(T))
	print("El valor del test chi cuadrado es {}".format(chi2))
	print("El valor de la simulacion es {}".format(sim))
	
if __name__ == "__main__":
	main()
