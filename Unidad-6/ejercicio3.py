from __future__ import print_function, division
from random import random

def F(x):
	return x

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

def main():
	"""
	Enunciado:
	Calcular  una  aproximación  del p−valor  de  la  hipótesis:  
	“Los  siguientes  10  números  son aleatorios”
	0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74
	
	"""
	Yi = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
	Yi.sort()

	n = len(Yi)
	Nsim = 1000

	D = estadistico_D(Yi, F) 
	KS = test_KS(n, Nsim, D)
	print("Valor del estadistico {}".format(D))
	print("Valor del test de KS {}".format(KS))
	
if __name__ == "__main__":
	main()
