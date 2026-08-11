from math import sqrt, exp

def lim_central(X: list, m: float, s: float):
    n = len(X)
    return (sum(X) - n*m) / ( sqrt(n) * s)

#distribucion empirica
def FDe(X:list, t:float):
    n = len(X)
    i = 0 
    for j in range(n):
        if X[j] <= t:
            i += 1 

    return i/n

#distribuciones analiticas
def FD_exp2(x):
    return 1 - exp(-2*x)

def FD_unif(x):
    if x < 0:
        return 0.0
    elif x > 1:
        return 1.0
    else:
        return x 
    
def FD_pareto(x):
    if x < 2:  # c es el valor mínimo posible, antes de eso la probabilidad es 0
        return 0
    else:
        return 1 - (2 / x)**3
