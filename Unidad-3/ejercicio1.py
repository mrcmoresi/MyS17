from __future__ import print_function
from random import random, shuffle

def permutacion(mazo):
	N = len(mazo)-1
	for i in range(N,0,-1):
		U = random()
		index = int(i*U)+1
		mazo[index], mazo[i] = mazo[i], mazo[index]
	return mazo

def main():
	exitos_mu = 0
	exitos_var = 0
	n = 100
	for _ in range(n):
		mazo = range(1,101)
		mazo_shuffle = permutacion(mazo)
		#print("mazo_shuffle",mazo_shuffle)
		exitos = sum([mazo_shuffle[i] == (i+1) for i in range(len(mazo))])
		#print("exitos",exitos)

		exitos_mu += exitos
		exitos_var += exitos**2
	esperanza = float(exitos_mu)/n
	varianza = float(exitos_var)/n - esperanza**2
	print("Esperanza: ", esperanza)
	print("Varianza: ", varianza)


if __name__ == "__main__":
	main()
