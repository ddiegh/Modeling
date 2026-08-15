from scipy.special import beta
from numpy import linspace, random

def dis_beta(a, b, x):    
    if 0<x<1: 
        return (x**(a-1) * (1-x)**(b-1)) / beta(a, b)
    
    else:
        return 0

def ej2(Pi: callable, x, y):
    if Pi(x) == 0:
        return 1
    
    else:
        return min(1, Pi(y) / Pi(x))

def paso(x, r, Pi):
    y = random.uniform(x-r, x+r)

    alpha_xy = ej2(Pi, x, y)

    u = random.uniform(0, 1)

    if u <= alpha_xy: 
        return y
    elif u > alpha_xy:
        return x


def metropolis_hastings(Xo, Pi, r, n):
    muestras = [Xo]
    for i in range(n):
        X = muestras[i]
        muestras.append( paso(X, r, Pi) )
        
    return muestras 

