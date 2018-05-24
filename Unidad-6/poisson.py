import math
import random
from distribuciones import *
from utils import *

##### Poisson no Homogeno #####

def mediaMuestralPoisson(muestra):
    """
    La muestra sera una lista de Ni, que son las observaciones del dia i
    """
    return sum(muestra)/float(len(muestra))


def varianzaMuestralPoisson(muestra):
    """
    La muestra sera una lista de Ni, que son las observaciones del dia i
    """
    media_muestral = mediaMuestralPoisson(muestra)

    suma = 0
    for valor in muestra:
        suma += (valor - media_muestral)**2

    varianza_muestral = suma/float(len(muestra) - 1)

    return varianza_muestral


def estadisticoTPoisson(media, varianza):
    """
    Estadistico del Proceso de Poisson no Homogeno.
    """
    return varianza/float(media)


def calcularPValor(muestra, k):
    """
    muestra = Ni's
    k = numero de simulaciones
    Si el P no se rechaza se pasa a prueba de Kruskal-Wallis, para ver si es Poisson.

    Paso 1
    Si p-valor es pequeno => se rechaza la hipotesis de que el numero de llegadas
    diarias sea de una va Poisson

    Paso 2
    Si no se rechaza la hipotesis entoces validamos con KW, si es muy chico el
    p-valor entoces se rechaza la hipotesis de que los tiempos de llegada vengan
    de un PPNH

    Paso 3
    Si no se rechaza la hipotesis PPNH => calculamos intensidad
    """
    media_muestral = mediaMuestralPoisson(muestra)
    varianza_muestral = varianzaMuestralPoisson(muestra)

    t = estadisticoTPoisson(media_muestral, varianza_muestral)

    r = len(muestra) # Tamano de la muestra

    m = media_muestral # Estimacion de la media (lambda)

    T_min = 0 # Cantidad de veces que Ti <= t
    T_max = 0 # Cantidad de veces que Ti >= t

    for _ in xrange(k):
        # Generamos r va Poisson con media m
        Y = [poisson(m) for _ in xrange(r)]

        media = mediaMuestralPoisson(Y)
        varianza = varianzaMuestralPoisson(Y)

        T = estadisticoTPoisson(media, varianza)

        if T <= t:
            T_min += 1

        if T >= t:
            T_max += 1

    p_valor = 2 * min(T_min/float(k), T_max/float(k))

    return p_valor


def kruskalWallis(muestra, rangoRi):
    """
    Chi-Cuadrado con r-1 grados de libertdad.
    r = cantidad de muestras
    Para ver si corresponden a una misma intensidad.
    """
    N = sum(muestra) # Numero total de llegadas
    r = len(muestra) # Tamano de la muestra

    # Calculamos es estadistico R
    p1 = 12.0/(N * (N+1))

    j = 0
    suma = 0
    for Ni in muestra:
        suma += (rangoRi[j] - (Ni*(N+1))/2.0)**2 / Ni
        j += 1

    R = p1 * suma

    chi = ji_cuadrado(r-1, R)

    p_valor = 2 * min(1-chi, chi)

    return p_valor


def intensidadLamda(muestra, t):
    """
    muestra = los tiempos de llegada (Ni)
    """
    r = len(muestra)
    for valor in muestra:
        if t > valor:
            yj_1 = valor
            yj = muestra[muestra.index(valor) + 1]
            break

    lamda_t = 1.0/((yj - yj_1)*r)

    return lamda_t


def ejemplo01():
    muestra = [18, 24, 16, 19, 25]
    Ri = [1010, 960, 1180, 985, 1118]

    print "p-valor Poisson =", calcularPValor(muestra, 10000)
    print "p-valor KW =", kruskalWallis(muestra, Ri)

ejemplo01()