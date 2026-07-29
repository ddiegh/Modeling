from random import uniform

def grad(f: callable, X: list, h: float = 1e-10) -> list:
    """
    Calcula el gradiente de una funcion en un punto especifico.
    """
    df = []
    for i in range(len(X)):
        #hacemos copias para no modificar la lista original con las diferencias finitas
        Y = X.copy()
        Z = X.copy()

        #incremento y decremento 
        Y[i] += h
        Z[i] -= h

        #derivada parcial i
        parcial = (f(Y)-f(Z)) / (2*h)

        df.append(parcial)
        
    return df


def descenso_gradiente(f: callable, Xo: list, a: float, iter: int):
    """
    Encuentra el minimo de una funcion.
    """

    n = len(Xo)
    X = [Xo]

    for _ in range(iter):
        Xn = X[-1]

        df = grad(f, Xn)
        X.append( [Xn[i] - a*df[i] for i in range(n)] )

    return X[-1]


def alg_evolutivo(f: callable, Xo: list, a: float, m: float, x_limits: list, y_limits: list, iter: int):
    #suponemos que estamos trabajando en dos dimensiones
    X = [Xo]

    for _ in range(iter):
        #generamos nuevos valores dependiendo de la probabilidad m
        p = uniform(0,1)
        xn, yn = X[-1][0], X[-1][1] 

        if p < m: #buscamos en todo el dominio
            x = uniform(x_limits[0], x_limits[1])
            y = uniform(y_limits[0], y_limits[1])

        else: #buscamos en el dominio mas chico
            x = uniform(xn-a, xn+a)
            y = uniform(yn-a, yn+a)

        #los valores deben estar en el dominio y cada vez ser menores
        if f([x,y]) < f([xn, yn]) and x_limits[0]<x<x_limits[1] and y_limits[0]<y<y_limits[1]:
            X.append([x,y])

    return X








