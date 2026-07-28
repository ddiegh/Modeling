# Metodo de Gauss-Jordan para diagonalizar matrices y descomposiciones LU y QR. 

## Introducción 
En esta practica se trabaja un poco con el algebra matricial numerica.
Se implementa la diagonalizacion de matrices mediante el metodo de Gauss-Jordan y la descomposicion LU y QR. 

## Requerimientos
El codigo funciona bastante bien sin otras librerias ya que se implementan funciones auxiliares, las cuales dividen los problemas principales en varias etapas.

Por ejemplo: para la diagonalización se ocupan dos funciones que hacen el trabajo pesado, una se encarga de escalonar la matriz en una triangular superior y la otra en una triangular inferior, juntando esto tenemos el metodo de Gauss-Jordan.

Solo se ocuparon dos funciones de Numpy: `identity` y `dot` las cuales facilitan los algoritmos, aunque se podrian implemetentar solo con python para mejorar la independencia del codigo.

## Explicación del codigo
### Metodo de Gauss-Jordan 
La idea de este algortitmo es ir escalonando nuestra matriz con operaciones elementales, primero hasta llegar a una matriz diagonal superior y luego llegar a la matriz diagonal. 

Partiendo de que se puede hacer el algoritmo en dos pasos, se crearon dos funciones las cuales combinandolas nos dan el metodo de gauss-jordan.

Primero se ocupa la eliminacion gaussiana, en donde debemos escoger un elemento pivote para ir haciendo cero todos los elementos debajo de el. `eliminacion_hacia_adelante` es lo que realiza
```python 

def eliminacion_hacia_adelante(A:list[list]):

    n = len(A)
    for i in range(n): 
        pivote = A[i][i]

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
```
De forma muy dual se hace la eliminacion hacia atras, con esos dos algoritmos ya tenemos el metodo de gauss jordan. 

### Descomposicion LU
La descompiscion LU se realiza de forma muy identica al escalonamiento que realiza la eliminacion gaussina. 

Ocupando el algoritmo de escalonamiento hacia adelante obtenemos la matriz U y la matriz L simplemente se obtiene de ir guardando las constantes que hacen cero abajo de la diagonal en el proceso de escalonamiento.

### Descomposicion QR
En esta desomposicion si debimos definir varias funciones auxiliares como: norma de un vector, producto punto, proyectar un vector sobre otro, transponer una matriz y gram schmit. 

El codigo funcionaría mejor si se implementan dos funciones más: crear matriz identidad y multiplicar matrices 

El corazon de la descomposicion QR es `gram-schmit` en donde obtenemos una base de vectores ortonormales (usando la proyeccion de vectores). Una vez ortonormalizados los vectores,se obtiene directo la matriz R, simplemente multiplicando $Q^t$ con $A$. 


