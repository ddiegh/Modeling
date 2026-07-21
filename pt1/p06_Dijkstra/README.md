# Algoritmo de Dijkstra 

## Introducción 

En esta practica vamos a implementar el algoritmo de dijkstra desde cero. 

El algoritmo de Dijkstra nos sirve para determinar el camino más corto en una grafica con pesos en las aristas, desde un vértice inicial, hacia el resto de los vértices. Así, para
nuestro nodo inicial A, tendremos un vector D que guardará al final del algoritmo las
distancias desde A hasta el resto de los nodos.

Para conocer el algoritmo se pueden consultar videos en youtube, como el siguiente:
 https://www.youtube.com/watch?v=LLx0QVMZVkk

Observaciones: En el algoritmo se trabajan con los siguientes datos

* MD. Una matriz de costos de las aristas del grafo, donde en MD[u,v] se almacena el
costo de la arista entre u y v
* ED. Conjunto que contendrá los vértices para los cuales ya se tiene determinado el
camino mínimo.
* D. Un arreglo unidimensional tal que D[v] es el costo del camino mínimo del vértice
origen al vértice v.
* O. Un arreglo unidimensional tal que P[v] es el vértice predecesor de v en el camino
mínimo que se tiene construido

## Implementación de dijkstra en python
La idea de implementar dijkstra desde cero es conocer y entender de una mejor forma como funciona el algoritmo. Tambien se busca no depender de bibliotecas externas como numpy para el manejo de las matrices, por ello es que solo se usan listas de python. 

---

Primero definimos el algortimo en una funcion la cual recibe la matriz de pesos y el vertices inicial (en forma de entero).

Creamos 4 listas que nos serviran para ir guardando los datos y saber cuando un nodo debe ser permanente o no, cuando deter el algoritmo, etc.


```python
def dijkstra(A:list[list], o:int)->tuple:

    n = len(A)

    #listas que vamos a ocupar 
    predecesores = [0 for _ in range(n)]
    distancias = [0 for _ in range(n) ]
    permanentes = [o]
    nodos_abiertos = []
```
El siguiente paso es inicializar el bucle, el cual solo se detendra cuando todos los nodos sean permanentes (ie que ya se encontraron todas las distancias minimas)

Primero vamos a fijar un nodo (el ultimo que entro a los permanentes) y de ahi vamos a explorar hacia que otros nodos se conecta (esto lo encontramos en la matriz, viendo en que posiciones hay valores de costo). Una vez que encontramos esas conexiones, las agregamos a la lista que guarda las posibles visitas del nodo *NF* y a los *nodos abiertos*


```python 

    while len(permanentes)<n:

        NF = permanentes[-1] 
        posibles_visitas = []  

        for i in range(n):

            if A[NF][i] != 0:
                posibles_visitas.append(i)
                nodos_abiertos.append(i)
```

Una vez que sabemos las conexiones del nodo fijo, pasamos a etiquetarlas. 

La etiqueta de costo será el peso que tiene la arista que va del nodo fijo más el costo que ya tenía el nodo fijo.

Se implementaron varios condicionales para la elección del costo que se mantendrá en los nodos. Dado que se debe mantener de etiqueta el valor minimo entre el costo nuevo o el que ya tenia, como la lista de costos inicio con 0s, eso podía causar problemas entonces por eso tuvimos que usar varios casos.

```python 

        for pv in posibles_visitas:
            etiqueta = A[NF][pv] + distancias[NF] 

            if distancias[pv] != 0:
                distancias[pv] = min(distancias[pv], etiqueta)
            else:
                distancias[pv] = etiqueta
            
            if min(distancias[pv], etiqueta) == etiqueta:
                predecesores[pv] = NF

```
Una vez que ya tenemos las etiquetas optimas que tendrán los nodos que conectan al nodo fijo, vamos a borrar las conexiones en la matriz de pesos para no confundirnos con que valores podrían tomar los siguientes nodos fijos.


Para la elección del nuevo nodo fijo se debe elegir el que tenga un menor costo (entre todos los que esten disponibles), entonces vamos a igualar cada nodo con su costo para poder saber cual es el de minimo valor y que sea el nuevo nodo fijo.

el argumento `key = lambda x: x[1]`lo que hace es solo fijarse en las segundas entradas de las tuplas en la lista de donde se esta buscando el minimo

```python
        #borramos las conexiones del nodo fijo
        for i in range(n): 
            A[NF][i] = 0
            A[i][NF] = 0

        visit_valor = zip([na for na in nodos_abiertos], [distancias[na] for na in nodos_abiertos])

        Nuev_nodo, x = min(visit_valor, key = lambda x: x[1])
```

Una vez hecho esto solo debemos agregar a permanentes el nuevo nodo y sacarlo de los nodos abiertos, para volver a iterar

Finalmente devolvemos las distancias minimas y los predecesores.
```python 
        #actualizamos
        permanentes.append(Nuev_nodo)
        nodos_abiertos.remove(Nuev_nodo)

    return distancias, predecesores
```

### Funciones extras
Despues del algoritmo dijkstra, tambien implementamos otras 3 funciones las cuales nos sirven para reconstruir la ruta de nodos en dijkstra, mostrar de forma mas sencilla las rutas y tambien saber la distancia minima entre dos puntos especificos

### Pruebas
Se probó el algoritmo con distintas matrices de pesos para ver como funcionaba y compararlo con otros modelos. 

Probaremos el algoritmo con la siguiente matriz de pesos:

| Nodo | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 0 |
| **1** | 3 | 0 | 1 | 0 | 4 | 0 | 0 | 0 |
| **2** | 0 | 1 | 0 | 3 | 0 | 2 | 2 | 0 |
| **3** | 2 | 0 | 3 | 0 | 0 | 0 | 4 | 0 |
| **4** | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 6 |
| **5** | 0 | 0 | 2 | 0 | 0 | 0 | 3 | 4 |
| **6** | 0 | 0 | 2 | 4 | 0 | 3 | 0 | 5 |
| **7** | 0 | 0 | 0 | 0 | 6 | 4 | 5 | 0 |

Primero escribimos la matriz con listas de python y pasamos a la funcion (en este caso la pasamos a la funcion que muestra las rutas bien) con el nodo inicial 0 
### Salida del algoritmo

Al ejecutar `mostrar_rutas(M1, 0)`, la terminal arroja el siguiente resultado con los costos mínimos y el *backtracking* de la ruta:

```text
La distancia del nodo inicial 0 al nodo 0 es de 0 siguiendo la ruta: [0, 0]
 La distancia del nodo inicial 0 al nodo 1 es de 3 siguiendo la ruta: [0, 1]
 La distancia del nodo inicial 0 al nodo 2 es de 4 siguiendo la ruta: [0, 1, 2]
 La distancia del nodo inicial 0 al nodo 3 es de 2 siguiendo la ruta: [0, 3]
 La distancia del nodo inicial 0 al nodo 4 es de 7 siguiendo la ruta: [0, 1, 4]
 La distancia del nodo inicial 0 al nodo 5 es de 6 siguiendo la ruta: [0, 1, 2, 5]
 La distancia del nodo inicial 0 al nodo 6 es de 6 siguiendo la ruta: [0, 1, 2, 6]
 La distancia del nodo inicial 0 al nodo 7 es de 10 siguiendo la ruta: [0, 1, 2, 5, 7]
```

Si utilizamos la función específica para consultar un solo destino con `distancia_puntos(M1, 0, 7)`, obtenemos:

```text
la distancia mas corta del punto 0 a 7 es de 10 siguiendo la ruta: [0, 1, 2, 5, 7]
```

Ambas funciones usadas anteriormente usan el modelo de dijkstra para encontrar estas rutas. 