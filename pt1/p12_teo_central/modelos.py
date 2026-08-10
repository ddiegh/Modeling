from math import sqrt

def lim_central(X: list, m: float, s: float):
    n = len(X)
    return (sum(X) - n*m) / ( sqrt(n) * s)

