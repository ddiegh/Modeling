
def dijkstra(A:list[list], o:int)->tuple:
    """
    Realiza el algoritmo de dijkstra para encontrar los caminos más cortos en una grafica con pesos.

    Args:
        A (list[list]): matriz de costos (nativa de python)
        o (int): nodo inicial

    Returns:
        tuple: (distancias minimas, ruta de predecesores)
    """


    n = len(A)

    #listas que vamos a ocupar 
    predecesores = [0 for _ in range(n)]
    distancias = [0 for _ in range(n) ]
    permanentes = [o]
    nodos_abiertos = []

    #bucle hasta que se tengan todos los nodos permanentes
    while len(permanentes)<n:

        NF = permanentes[-1] #nodo fijo

        #visitas que tiene el nodo NF 
        posibles_visitas = []  
        for i in range(n):
            if A[NF][i] != 0:
                posibles_visitas.append(i)
                nodos_abiertos.append(i)

        #etiquetamos cada posible visita del nodo fijo (costo y predecesor)
        for pv in posibles_visitas:
            etiqueta = A[NF][pv] + distancias[NF]  #distancia acumulada

            #dado que distancias se creó con ceros, debemos separar en casos para ver cual si se mantiene el costo o cambia
            if distancias[pv] != 0:
                distancias[pv] = min(distancias[pv], etiqueta)
            else:
                distancias[pv] = etiqueta
            
            #registro del antecesor
            if min(distancias[pv], etiqueta) == etiqueta:
                predecesores[pv] = NF


        #borramos las conexiones del nodo fijo porque ya es permanente 
        for i in range(n): 
            A[NF][i] = 0
            A[i][NF] = 0

        #emparejamos los posibles nodos permanentes con el costo que tienen para decidir
        visit_valor = zip([na for na in nodos_abiertos], [distancias[na] for na in nodos_abiertos])

        Nuev_nodo, x = min(visit_valor, key = lambda x: x[1])

        #actualizamos
        permanentes.append(Nuev_nodo)
        nodos_abiertos.remove(Nuev_nodo)

    return distancias, predecesores



def reconstruir_ruta(A:list[list], o:int):
    """
    Reconstrucción de las rutas más cortas del algoritmo dijkstra usando backtracking
    """

    distancias, predecesores = dijkstra(A, o)

    todas_las_rutas = []
    for i, predecesor in enumerate(predecesores):
        
        rutas = [predecesor]
        anterior = predecesor
        
        #la ruta debe empezar en el nodo inicial. 
        while rutas[-1] != o:  
            anterior = predecesores[rutas[-1]]
            rutas.append(anterior)
        
        #agregamos el nodo final 
        rutas.insert(0, i)
        rutas.reverse()
        todas_las_rutas.append(rutas)

    return todas_las_rutas, distancias


def mostrar_rutas(A:list[list], o:int):
    """
    Mostrar las rutas de dijkstra de una forma más simple de entender.
    """

    rutas, distancias = reconstruir_ruta(A, o)

    for i in range(len(rutas)):
        print(f" La distancia del nodo inicial {o} al nodo {i} es de {distancias[i]} siguiendo la ruta: {rutas[i]}")


def distancia_puntos(A:list[list], a:int, b:int):
    """
    Distancia minima entre dos puntos usando el algoritmo de dijkstra.
    """
    rutas, distancias = reconstruir_ruta(A, a)
    print(f"la distancia mas corta del punto {a} a {b} es de {distancias[b]} siguiendo la ruta {rutas[b]}")

