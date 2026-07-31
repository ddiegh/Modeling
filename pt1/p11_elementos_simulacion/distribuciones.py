from random import uniform
from numpy import log

def bernoulli(p):
    u = uniform(0, 1)
    if u < p:
        return 0
    else:
        return 1
    
def geom(p):
    contador = 0

    while bernoulli(p) == 0:
        contador += 1
        
    return contador

def exp(lamb):
    y = uniform(0,1)
    return -1/lamb * log(1-y)


def pareto(c, alpha):
    u = uniform(0, 1)
    return c / ( (1-u)**(1/alpha) )


