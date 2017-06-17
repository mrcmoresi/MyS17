from __future__ import division, print_function
from random import random
from math import log, exp, sqrt

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def exponencial(lamb):
	#VA continua con distribucion exponencial de parametro lambda
	#X ~ E(lamb)
	U = random()
	return (-log(U) / float(lamb))

def repairModel(N, S, mean_fail, mean_repair):
	#N number of washing machines working correctly
	#S number of washing machines spared
	#r number of wm to be repaired
	#mean_fail mean time until a machine fail
	#mean_repair mean time to repair a machine

	#uptime
	t = 0
	#number of disable machines
	r = 0
	#time need to repair the first
	time_to_repare = np.inf

	T = 0

	tf = []

	#genero los tiempos de falla para cada lavarropas
	for _ in range(N):
		time_until_fail = exponencial(1 / float(mean_fail))
		tf.append(time_until_fail)

	#ordeno la lista de modo creciente
	tf.sort()

	while True:
		#Case 1: se rompe la lavadora antes de que la que se esta reparando este lista
		if tf[0] < time_to_repare:
			t = tf[0] #avanzo hasta el primer tiempo
			r += 1 #aumento la cantidad de lavarropas rotos
			if r == S+1: #No hay mas maquinas disponibles entonces termino
				T = t #guardo el tiempo de vida que tuvo
				break #termino el ciclo
			if r < S+1: #Caso en el que hay algun lavarropa de repuesto
				new_machine = exponencial(1/float(mean_fail)) #tiempo en el cual va a fallar la lavadora que incorporamos
				tf[0] = t + new_machine #cambio la que se rompio por la nueva en las lista de lavarropas actuales considerando el tiempo donde estoy parado
				tf.sort() #ordeno de modo creciente
			if r == 1: 
				# En este caso no habia ninguna lavadora rota por lo tanto arranca la reparacion de inmediato
				#y se completa en t + new_reparation osea el tiempo actual mas lo que demora
				new_reparation = exponencial(1/float(mean_repair))
				time_to_repare = t + new_reparation
		elif tf[0] >= time_to_repare:
			#en este caso la primer lavarropa que se rompe se rompe despues del tiempo necesario para reparar la que estaba en el taller
			t = time_to_repare #avanzo el tiempo hasta el punto que se que no se rompe nada
			r -= 1 #en este punto del tiempo ya pude reparar la que se estaba arreglando
			if r > 0:
				#si todavia quedan por arreglar
				#Pongo una maquina a reparar, tengo que ver cuanto va a demorar
				new_reparation = exponencial(1/float(mean_repair))
				time_to_repare = t + new_reparation
			if r == 0:
				#Caso en el que no hay lavarropas para reparar, entonces el seteo el tiempo en infinito
				time_to_repare = np.inf

	return	T


def repairModel_2(N, S, mean_fail, mean_repair):
	#N number of washing machines working correctly
	#S number of washing machines spared
	#r number of wm to be repaired
	#mean_fail mean time until a machine fail
	#mean_repair mean time to repair a machine

	#uptime
	t = 0
	#number of disable machines
	r = 0
	#time need to repair the first
	time_to_repare = []
	for _ in range(S):
		time_to_repare.append(np.inf)
	time_to_repare.sort()
	T = 0

	tf = []

	#genero los tiempos de falla para cada lavarropas
	for _ in range(N):
		time_until_fail = exponencial(1 / float(mean_fail))
		tf.append(time_until_fail)

	#ordeno la lista de modo creciente
	tf.sort()
	while True:
		#Case 1: se rompe la lavadora antes de que la que se esta reparando este lista
		min_repair = min(time_to_repare)
		if tf[0] < min_repair:
			t = tf[0] #avanzo hasta el primer tiempo
			r += 1 #aumento la cantidad de lavarropas rotos
			if r == S+1: #No hay mas maquinas disponibles entonces termino
				T = t #guardo el tiempo de vida que tuvo
				break #termino el ciclo
			if r < S+1: #Caso en el que hay algun lavarropa de repuesto
				new_machine = exponencial(1/float(mean_fail)) #tiempo en el cual va a fallar la lavadora que incorporamos
				tf[0] = t + new_machine #cambio la que se rompio por la nueva en las lista de lavarropas actuales considerando el tiempo donde estoy parado
				tf.sort() #ordeno de modo creciente
			if r == 1 or r == 2: 
				# En este caso no habia ninguna lavadora rota por lo tanto arranca la reparacion de inmediato
				#y se completa en t + new_reparation osea el tiempo actual mas lo que demora
				new_reparation = exponencial(1/float(mean_repair))
				if time_to_repare[0] is np.inf:
					time_to_repare[0] = t + new_reparation 
				elif time_to_repare[1] is np.inf:
					time_to_repare[1] = t + new_reparation

		elif tf[0] >= min_repair:
			#en este caso la primer lavarropa que se rompe se rompe despues del tiempo necesario para reparar la que estaba en el taller
			t = min_repair #avanzo el tiempo hasta el punto que se que no se rompe nada
			r -= 1 #en este punto del tiempo ya pude reparar la que se estaba arreglando
			if r > 1:
				#si todavia quedan por arreglar
				#Pongo una maquina a reparar, tengo que ver cuanto va a demorar
				new_reparation = exponencial(1/float(mean_repair))
				time_to_repare[time_to_repare.index(min_repair)] = t + new_reparation
				time_to_repare.sort()
			if r <= 1:
				#Caso en el que no hay lavarropas para reparar, entonces el seteo el tiempo en infinito
				time_to_repare[time_to_repare.index(min_repair)] = np.inf
				time_to_repare.sort()

	return	T


def esperanzayVarianza(n, N, S, mean_fail, mean_repair):
	"""

	calculo de la esperanza y varianza del tiempo de fallo del sistema del lavadero
	devuelve (esperanza, varianza, desviacion std)

	"""
	lst = []
	X1 = 0.0
	X2 = 0.0
	for _ in range(n):
		T = repairModel(N, S, mean_fail, mean_repair)
		X1 += T
		X2 += T**2
		lst.append(T)
	esperanza = X1/float(n)
	varianza = X2/float(n) - (esperanza ** 2)  # V(x) = E(X^2) - E(x)^2

	desviacion_std = sqrt(varianza)

	return esperanza, varianza, desviacion_std, lst

def esperanzayVarianza_2(n, N, S, mean_fail, mean_repair):
	"""

	calculo de la esperanza y varianza del tiempo de fallo del sistema del lavadero
	devuelve (esperanza, varianza, desviacion std)

	"""
	lst = []
	X1 = 0.0
	X2 = 0.0
	for _ in range(n):
		T = repairModel_2(N, S, mean_fail, mean_repair)
		X1 += T
		X2 += T**2
		lst.append(T)
	esperanza = X1/float(n)
	varianza = X2/float(n) - (esperanza ** 2)  # V(x) = E(X^2) - E(x)^2

	desviacion_std = sqrt(varianza)

	return esperanza, varianza, desviacion_std, lst


def main():
	n = 10000
	N = 5
	S = 2
	mean_fail = 1
	mean_repair = 1/8.0
	#N = 5   S =2  1 Tecnico
	esp, var, std, lst = esperanzayVarianza(n, N,S,mean_fail, mean_repair)
	print("Esperanza = ", esp)
	print("Varianza = ", var)
	print("Desviacion Standar = ", std)

	#S =2 N = 5, 2 tecnicos
	esp_2, var_2, std_2, lst_2 = esperanzayVarianza_2(n, N, S, mean_fail, mean_repair)
	
	print("\nEsperanza ejer 2 = ", esp_2)
	print("Varianza ejer 2 = ", var_2)
	print("Desviacion Standar ejer 2 = ", std_2)


	esp_3, var_3, std_3, lst_3 = esperanzayVarianza(n, N,3,mean_fail, mean_repair)
	print("\nEsperanza = ", esp_3)
	print("Varianza = ", var_3)
	print("Desviacion Standar = ", std_3)


	#plt.hist([lst,lst_2,lst_3], bins=100, color=['r','g','b'], alpha=[1.0,0.5,0.3], edgecolor='black', normed=True, label="prueba", histtype='barstacked', stacked=True)
	#FIGURA 1
	plt.figure(1)
	plt.hist(lst, bins=np.arange(0,14,0.2), color='r', alpha=0.8, edgecolor='black', normed=True, histtype='barstacked', stacked=True)
	plt.hist(lst_2, bins=np.arange(0,14,0.2), color='b', alpha=0.5, edgecolor='black', normed=True, histtype='barstacked', stacked=True)

	red_patch = mpatches.Patch(color='red', label='5 en Operancion, 2 Repuestos, 1 Tecnico')
	green_patch = mpatches.Patch(color='blue', label='5 en Operancion, 2 Repuestos, 2 Tecnicos')
	purple_patch = mpatches.Patch(color='purple', label='Interseccion de los datos')

	plt.legend(handles=[red_patch, green_patch, purple_patch])
	plt.xlabel("Cantidad de Meses")
	plt.ylabel("Frecuencia de Fallo")
	plt.title("Sistema actual contra la incorporacion de un tecnico")
	plt.xticks(range(14))
	plt.xlim(0,14)

	#FIGURA 2
	plt.figure(2)
	plt.hist(lst, bins=np.arange(0,14,0.2), color='r', alpha=0.8, edgecolor='black', normed=True, histtype='barstacked', stacked=True)
	plt.hist(lst_3, bins=np.arange(0,14,0.2), color='b', alpha=0.5, edgecolor='black', normed=True, histtype='barstacked', stacked=True)

	red_patch = mpatches.Patch(color='red', label='5 en Operancion, 2 Repuestos, 1 Tecnico')
	blue_patch = mpatches.Patch(color='blue', label='5 en Operancion, 3 Repuestos, 1 Tecnico')
	purple_patch = mpatches.Patch(color='purple', label='Interseccion de los datos')

	plt.legend(handles=[red_patch, blue_patch, purple_patch])
	plt.xlabel("Cantidad de Meses")
	plt.ylabel("Frecuencia de Fallo")
	plt.title("Sistema actual contra la incorporacion de una lavadora")
	plt.xticks(range(14))
	plt.xlim(0,14)
	

	#FIGURA 3
	plt.figure(3)
	plt.hist(lst_2, bins=np.arange(0,14,0.2), color='r', alpha=0.8, edgecolor='black', normed=True, histtype='barstacked', stacked=True)
	plt.hist(lst_3, bins=np.arange(0,14,0.2), color='b', alpha=0.5, edgecolor='black', normed=True, histtype='barstacked', stacked=True)

	red_patch = mpatches.Patch(color='red', label='5 en Operancion, 2 Repuestos, 2 Tecnicos')
	blue_patch = mpatches.Patch(color='blue', label='5 en Operancion, 3 Repuestos, 1 Tecnico')
	purple_patch = mpatches.Patch(color='purple', label='Interseccion de los datos')

	plt.legend(handles=[red_patch, blue_patch, purple_patch])
	plt.xlabel("Cantidad de Meses")
	plt.ylabel("Frecuencia de Fallo")
	plt.title("Comparacion entre las opciones a implementar")
	plt.xticks(range(14))
	plt.xlim(0,14)

	
	#FIGURA 4
	plt.figure(4)
	plt.hist(lst, bins=np.arange(0,14,0.2), color='r', alpha=0.8, edgecolor='black', normed=True, histtype='barstacked', stacked=True)	
	plt.hist(lst_2, bins=np.arange(0,14,0.2), color='cyan', alpha=0.5, edgecolor='black', normed=True, histtype='barstacked', stacked=True)
	plt.hist(lst_3, bins=np.arange(0,14,0.2), color='yellow', alpha=0.3, edgecolor='black', normed=True, histtype='barstacked', stacked=True)

	red_patch = mpatches.Patch(color='red', label='5 en Operancion, 2 Repuestos, 1 Tecnicos')
	cyan_patch = mpatches.Patch(color='cyan', label='5 en Operancion, 2 Repuestos, 2 Tecnicos')
	yellow_patch = mpatches.Patch(color='yellow', label='5 en Operancion, 3 Repuestos, 1 Tecnico')
	purple_patch = mpatches.Patch(color='purple', label='Interseccion de los datos')

	#plt.legend(handles=[red_patch, cyan_patch, yellow_patch])
	plt.xlabel("Cantidad de Meses")
	plt.ylabel("Frecuencia de Fallo")
	plt.title("Comparacion entre las opciones a implementar")
	plt.xticks(range(14))
	plt.xlim(0,14)
	plt.show()



if __name__ == "__main__":
	main()
