from __future__ import print_function, division
from utils import estadistico_D, test_KS, debo_rechazar, estadistico_ji, ji_cuadrado
from scipy.stats import binom


def F(x, n, p):
	#Binomial de parametro n p
	return binom.pmf(x, n, p)

def main():
	
	"""
	Calcular una aproximación del p−valor de la prueba
	de que los siguientes datos corresponden a una 
	distribución binomial con parámetros(n=8,p), 
	donde p no se conoce: 6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7.
	
	"""
	
	Yi = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
	Yi.sort()
	n = 8
	k = 8
	#Si X ~ Binomial(n,p)
	#Se que E[X] = n.p
	#El estimador X_barra es insesgado para la esperanza
	#por lo tanto E[X] = X_barra => X_barra = n.p => p_sombrero = X_barra / n
	X_bar = sum(Yi)/float(len(Yi))

	p_sombrero = X_bar / float(n)
	
	#construyo las frecuencias de la muestra
	Ni = [Yi.count(i+1) for i in range(n)] 
	pi = []
	for j in range(n):
		pi.append(F(j+1, 8, p_sombrero))
	
	T = estadistico_ji(n, len(Yi), Ni, pi)
	#en este caso que se estimo el 1 parametro los dof son k - m -1 donde m es la cantidad de parametros estimados
	test_chi = ji_cuadrado(T, dof = k - 2)
	print("El estadistico T tiene el valor de {}".format(T))
	print("El p-valor obtenido por el test chi cuadrado es {}".format(test_chi))

if __name__ == "__main__":
	main()
	

