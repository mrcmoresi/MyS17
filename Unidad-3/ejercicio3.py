from __future__ import print_function
from random import random

def ejercicio3(n):
	X = 0
	X2 = 0
	for _ in range(n):
		dados_results = {}
		lanzamientos = 0
		for i in range(2,13,1):
			dados_results[i] = 0
	
		while(0 in dados_results.values()):
			dado_1 = int(6*random())+1
			dado_2 = int(6*random())+1
			dados_results[dado_1+dado_2] += 1
			lanzamientos += 1
		#para calcular la esperanza
		X += lanzamientos #X
		#para calcular la varianza
		X2 += lanzamientos**2 #X**2
	esperanza = X/float(n)
	varianza = X2/float(n) - (esperanza)**2 #Var(x) = E(x^2) - E(x)^2 
	return esperanza, varianza
		

def main():
	for n in [100, 1000, 10000, 100000]:
		esperanza, varianza = ejercicio3(n)
		print("n=", n, "E(X)=", esperanza, "Var(X)=", varianza)

if __name__ == "__main__":
	main()
