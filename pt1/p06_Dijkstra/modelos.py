
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

        #me marcaba ese error 
        if len ([distancias[pv] for pv in posibles_visitas]) == 0:
            break

        else: 
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


