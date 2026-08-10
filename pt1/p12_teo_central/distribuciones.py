from random import uniform
from numpy import log

def exp(lamb):
    y = uniform(0,1)
    return -1/lamb * log(1-y)


def pareto(c, alpha):
    u = uniform(0, 1)
    return c / ( (1-u)**(1/alpha) )

