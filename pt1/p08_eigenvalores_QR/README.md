# Calculo de eigenvalores usando metodo QR.

El método QR se basa en el hecho de que a una matriz real A de tamaño n×n se le puede
calcular la factoriazción QR de forma que
A=QR
Donde Q es ortogonal y R es triangular superior. 

El método QR se define de la siguiente
manera:

$$A_m = R_{m-1} Q_{m-1}$$

en donde $Q_{m-1}$ y $R_{m-1}$ es la factorización QR de la matriz $A_{m-1}$

Conforme m crece los valores propios de Am se aproximan a los valores propios de A.

## Implementación
La implementación del algoritmo se da de forma natural al tener el modelo matematico. Agregamos una condición de paro en la que el ciclo se rompe en caso de que los elementos abajo de la diagonal ya sean muy ceranos a cero. 

```python 
    if error < tol:
        break
```

Esta condicion de paro nos sirve para evitar errores numericos que se pueden dar a la hora de las descomposiciones. 

## Ejemplo de uso 
Hicimos una prueba del modelo con la matriz
|  | | |
| :---: | :---: | :---: |
| 3 | -1 | 1 |
| -1 | 5 | -1 |
| 1 | -1 | 3 |

cuyos eigenvalores reales son 6,3,2

```python 
    A = [
    [3.0, -1.0,  1.0],
    [-1.0, 5.0, -1.0],
    [1.0, -1.0,  3.0]]

    print(eigenvalores(A))
```

```python
>>> Convergencia en 56 iteraciones
[[ 6.00000000e+00 -2.84960329e-16  2.69261518e-16]
 [-2.94392336e-17  3.00000000e+00  7.49466800e-11]
 [ 2.20641291e-27  7.49467154e-11  2.00000000e+00]]

```

Podemos ver que efectivamente en la diagonal tenemos los eigenvalores y en las demas entradas valores muy cercanos al cero, de igual forma podemos ver que hubo una convergencia bastante rapida.

