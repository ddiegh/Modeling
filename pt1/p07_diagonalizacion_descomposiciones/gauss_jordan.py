## en este archivo estan las funciones que implementan el metodo de Gauss-Jordan para diagonalizar matrices.

def eliminacion_hacia_adelante(A:list[list])->list[list]:
    """
    Realiza el metodo de gauss (eliminacion gaussina) para escalonar una matriz cuadrada. 

    Args:
        A(list[list]): Matriz cuadrada que se desea escalonar.

    Returns:
        list[list]: Matriz escalonada (triangular superior)
    """

    n = len(A)
    for i in range(n): 
        pivote = A[i][i]
        # intercambiar renglones en caso de que el pivote sea cero
        if pivote == 0:
            #encontrar el renglon pivote bueno
            j = i+1
            while pivote == 0:
                A[i], A[j] = A[j], A[i]
                j += 1

        #hacemos 1 al pivote 
        A[i] = [k / pivote for k in A[i]]
        
        #hacemos ceros abajo del pivote
        for j in range(i+1, n):
            A[j] = [k - A[j][i]*z for k,z in zip(A[j], A[i])]

        A[i] = [k*pivote for k in A[i]]

    return A

def eliminacion_hacia_atras(A:list[list])->list[list]:
    """
    Escalona una matriz cuadrada a su forma triangular inferior.

    Args:
        A(list[list]): Matriz cuadrada que se desea escalonar.

    Returns:
        list[list]: Matriz escalonada (triangular inferior)
    """

    n = len(A)
    for i in range(n-1, -1, -1): 
        pivote = A[i][i]

        if pivote == 0:
            #encontrar el renglon pivote bueno
            j = i-1
            while pivote == 0:
                A[i], A[j] = A[j], A[i]
                j -= 1

        #hacemos 1 al pivote 
        A[i] = [k / pivote for k in A[i]]
        
        #hacemos ceros arriba del pivote
        for j in range(i-1, -1, -1):
            A[j] = [k - A[j][i]*z for k,z in zip(A[j], A[i])]

        A[i] = [k*pivote for k in A[i]]

    return A

def gauss_jordan(A:list[list])->list[list]:
    """
    Diagonaliza una matriz cuadrada usando el metodo de gauss-jordan.

    Args:
        A(list[list]): Matriz cuadrada que se desea diagonalizar.

    Returns:
        list[list]: Matriz diagonalizada.
    """

    sup = eliminacion_hacia_adelante(A)
    diag = eliminacion_hacia_atras(sup)

    return diag


matriz_prueba = [
    [2.0,  1.0, -1.0],
    [4.0,  5.0,  0.0],
    [2.0, -2.0, -1.0]
]
A = [[1, -2, -3], [2,1,1], [1, 3, -2]]

print(eliminacion_hacia_adelante(A))



