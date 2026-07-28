def newton_raphson(f: callable, df: callable, xo: float, epsilon: float, max_iter: int):
    """
    Aplica el método de Newton-Raphson para encontrar una raíz de la función f.

    Args:
        f (callable): Función de la cual se busca la raíz.
        df (callable): Derivada de f.
        xo (float): Aproximación inicial (x0).
        epsilon (float): Tolerancia del algoritmo. La iteración para cuando
            |f(x_n)| < epsilon.
        max_iter (int): Número máximo de iteraciones permitidas en caso de que
            no se alcance la tolerancia.

    Returns:
        list[float]: Lista con todos los valores de las iteraciones, comenzando
            por xo y terminando en la última aproximación.
    """
    
    x = [xo]
    i = 0

    while abs(f(x[-1]))>epsilon and i<max_iter:
        xn = x[-1]
        x.append(xn - (f(xn)/df(xn)))
        i += 1
    return x


def punto_fijo(xo: float, g: callable, epsilon: float, max_iter: int):
    """
    Realiza el metodo de punto fijo para encontrar raices en una funcion. 

    Args:
        xo (float): Aproximación inicial (x0).
        g (callable): Función de iteración del punto fijo.
        epsilon (float): Tolerancia del algoritmo. La iteración para cuando
            |g(x_n) - x_n| < epsilon.
        max_iter (int): Número máximo de iteraciones permitidas en caso de que
            no se alcance la tolerancia.

    Returns:
        list[float]: Lista con todos los valores de las iteraciones, comenzando
            por xo y terminando en la última aproximación calculada.
    """

    x = [xo]

    i = 0 
    while abs( g(x[-1]) - x[-1] ) > epsilon and i < max_iter:
        x.append(g(x[-1]))
        i += 1

    return x

