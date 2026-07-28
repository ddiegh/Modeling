
from numpy import dot as dt

## Algunas funciones auxiliares 
def norm(x:list)->float:
    return (sum(xi**2 for xi in x))**0.5

def dot(x:list, y:list)->float:
    return sum(xi*yi for xi, yi in zip(x, y))

def transpose(A:list[list]):
    n = len(A)  #renglones
    m = len(A[0]) #columnas

    At = []

    for i in range(m):
        renglon = []
        for j in range(n):
            renglon.append(A[j][i])
        At.append(renglon)

    return At

def proy(x:list, y:list):
    """
    Proyeccion del vector x sobre y.
    """
    return [(dot(x, y)/dot(x, x))*xi for xi in x] 


def gram_schmidt(A: list[list]):
    """
    Realiza el proceso de ortogonalización de Gram-Schmidt en una matriz.

    Args:
        A (list[list]): matriz sobre la que se aplica el proceso.

    Returns:
        Matriz ortonormal del mismo tamaño que A.
    """

    A_t = transpose(A)

    U_0 = A_t[0]
    U = [U_0]  #el primer vector se queda igual

    for i in range(1, len(A_t)):
        acum_proy = [0 for _ in range(len(A_t[0]))] #acumulador de proyecciones

        vector_vi = A_t[i]

        for j in range(i):
            vector_uj = U[j]
            #sumamos lo acumulado con la nueva proyeccion
            acum_proy = [acum + p for acum, p in zip(acum_proy, proy(vector_uj, vector_vi))]

        #ya tenemos todas las proyecciones, solo hacemos la resta entre los vectores
        suma = [a - b for a, b in zip(vector_vi, acum_proy)]
        U.append(suma)

    #normalizamos cada vector 
    for i, columa in enumerate(U):
        U[i] = [ui/norm(columa) for ui in columa]

    return transpose(U) 

def qr(A:list[list])->tuple:
    """
    Realiza la factorización QR de una matriz. 

    Args:
        A (list[list]): Matriz inicial que se va a factorizar

    Returns:
        tuple: matrices Q, R
    
    """
    Q = gram_schmidt(A)
    Q_t = transpose(Q)

    R = dt(Q_t, A)

    return Q, R

