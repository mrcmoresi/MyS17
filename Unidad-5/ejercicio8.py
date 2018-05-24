# -*- coding: utf-8 -*-

from random import random
import math
from distribuciones import *
import numpy as np
"""
Considerar un sistema con un unico servidor en el cual los clientes
potenciales llegan de acuerdo con un proceso de Poisson de razon 4.0.
Un cliente potencial entrara al sistema solo si hay tres o
menos clientes en el sistema al momento de su llegada. El tiempo
de servicio de cada cliente esta distribuido
segun una exponencial de parámetro 4.2. Despues del instante
T=8 no entran mas clientes al sistema (los
tiempos están dados en horas). Realizar un estudio de simulacion
para estimar el tiempo promedio que
un cliente pasa en el sistema. Aplicar el método “bootstrap”
para estudiar el error cuadratico medio de su
estimador.
"""

def tiempoServer():
    INFINITO = np.inf
    Na = 0
    Nd = 0
    Ta = [poisson(4.0), poisson(4.0), poisson(4.0)]
    Td = [INFINITO, INFINITO, INFINITO]
    n = 0
    T = 8
    A = [[], [], []]
    D = [[], [], []]
    t = 0

    while True:
        minimaEntrada = min(Ta)
        minimaDemora = min(Td)
        if minimaEntrada <= minimaDemora and minimaEntrada <= T:
            t = minimaEntrada
            Na += 1
            n += 1
            A[Ta.index(minimaEntrada)].append(t)
            Ta[Ta.index(minimaEntrada)] = poisson(4.0) + t
            if n <= 3:
                Y = exponencial(4.2)
                Td[Td.index(max(Td))] = t + Y

        elif minimaDemora < minimaEntrada and minimaDemora <= T:
            t = minimaDemora
            n -= 1
            Nd += 1
            D[Td.index(minimaDemora)].append(t)
            if n < 3:
                Td[Td.index(minimaDemora)] = INFINITO

            else:
                Y = exponencial(4.2)
                Td[Td.index(max(Td))] = t + Y

        elif min(minimaEntrada, minimaDemora) > T and n > 0:
            t = minimaDemora
            n = n - 1
            Nd += 1
            if n > 0:
                Y = exponencial(4.2)
            D[Td.index(minimaDemora)].append(t)

        elif min(minimaEntrada, minimaDemora) > T and n == 0:
            T = max(t - T, 0)
            break

    return T, A, D

def main():
    print(tiempoServer())

if __name__ == "__main__":
    main()