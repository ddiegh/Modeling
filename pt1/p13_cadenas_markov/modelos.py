from random import uniform
import numpy as np

def estado(v:list):
    """
    Regresa un estado aleatoriamente, tomando en cuenta las probabilidades que tiene cada estado.
    Funciona como simular un dado cargado 
    """

    #suponemos que el vector de probabilidades suma 1 
    k = len(v)
    u = uniform(0, 1)

    probas_acumuladas = 0
    for i in range(k):
        probas_acumuladas += v[i]
        if u < probas_acumuladas:
            return i


def cadena_markov_recorrido(P: np.array, qo: list, iter: int = 100):
    """
    Devuelve los estados de una cadena de markov.
    """

    estado_act = estado(qo)
    estados = [estado_act]

    for _ in range(iter):
        dist_actual = P[estados[-1]]

        estado_act = estado(dist_actual)
        estados.append(estado_act)

    return estados


def cadena_markov_busqueda(P: np.array, pi_0: list, estado_busqueda: int, max_iter: int):
    """
    Devuelve la cantidad de estados anteriores hasta llegar al estado objetivo.
    """
    estado_act = estado(pi_0)
    estados = [estado_act]

    i = 0
    while (estados[-1] != estado_busqueda) and (i < max_iter):

        dist_actual = P[estados[-1]]

        estado_act = estado(dist_actual)
        estados.append(estado_act)

        i += 1

    return len(estados)
