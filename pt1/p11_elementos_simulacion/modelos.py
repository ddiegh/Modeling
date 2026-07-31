from random import uniform

def parcial(X:list):
    """
    Realiza la suma parcial de una lista de variables aleatorias.
    """
    S = [] #sumas parciales 
    n = len(X)
    for k in range(n):
        suma = 1/(k+1) * sum(X[:k+1])
        S.append(suma)

    return S


def dado_justo(k: int):
    """
    Simula un dado justo y devuelve la cara que salió.
    """
    u = uniform(0, 1)

    for i in range(k):
        if u < (i+1)/k:
            return i+1


def dado_cargado(probas: list):
    """
    Simula un dado cargado. Devuelve la cara que cayó.
    """

    #suponemos que sum(probas) == 1
    k = len(probas)
    u = uniform(0, 1)

    probas_acumuladas = [sum(probas[:i+1]) for i in range(k)]

    for i in range(k):
        if u < probas_acumuladas[i]:
            return i+1


