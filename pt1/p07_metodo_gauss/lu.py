from numpy import identity, array

def lu(A:list[list])->tuple:
    """
    Realiza la descomposición LU de una matriz.

    Args:
        A(list[list]): Matriz cuadrada.

    Returns:
        tuple: Matrices L,U.
    """

    n = len(A)
    L = identity(n)
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
        
        #hacemos ceros abajo del pivote y agregamos en la matriz L los valores correspondientes
        for j in range(i+1, n):
            L[j][i] = A[j][i]/pivote
            A[j] = [k - A[j][i]*z for k,z in zip(A[j], A[i])]

        A[i] = [k*pivote for k in A[i]]

    U = array(A)
    return L, U


A = [[1, -2, -3], [2,1,1], [1, 3, -2]]

print(lu(A))