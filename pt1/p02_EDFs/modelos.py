def crec_exp(k):
    Po = 2 
    P = [Po]
    for _ in range(49):
        P.append(k*P[-1])
    return P 

def logistica(Po):
    r = 0.5
    k = 1000
    P = [Po]

    for _ in range(40):
        Pn = P[-1]
        P.append(Pn + (r*Pn * (1-(Pn/k))))
    return P

def lineal(r,b,Xo=1):
    X = [Xo]
    for _ in range(20):
        Xn = r*X[-1] + b 
        X.append(Xn)
    return(X)

def solucion(x):
    return -3*x**2 + 3*x + 2

def sol_DF(delta):
    Yo = 2 
    Y = [Yo]

    for t in range(19): 
        xn = t * delta 
        Yn = Y[-1]
        Y.append(Yn + (-6 * xn + 3) * delta)
            
    return Y