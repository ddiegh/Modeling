import numpy as np 

def Dijkstra(A:list[list], o:int):
    n = len(A)

    predecesores = [0 for _ in range(n)]
    distancias = [0 for _ in range(n) ]

    permanentes = [o]

    while len(permanentes)<n:

        NF = permanentes[-1] #nodo fijo

        #visitas que tiene el nodo NF
        posibles_visitas = []  
        for i in range(n):
            if A[NF][i] != 0:
                posibles_visitas.append(i)

        #etiquetamos cada posible visita del nodo fijo 
        for pv in posibles_visitas:
            etiqueta = A[NF][pv] + distancias[NF]  #distancia acumulada 
            if distancias[pv] != 0:
                distancias[pv] = min(distancias[pv], etiqueta)
            distancias[pv] = etiqueta

        if len ([distancias[pv] for pv in posibles_visitas]) == 0:
            break

        else: 
            #borramos las conexiones del nodo fijo porque ya es permanente 
            for i in range(n): 
                A[NF][i] = 0
                A[i][NF] = 0

            #enparejamos las posibles visitas con el costo que tienen
            visit_valor = zip([pv for pv in posibles_visitas], [distancias[pv] for pv in posibles_visitas])

            Nuev_nodo, x = min(visit_valor, key = lambda x: x[1])

            permanentes.append(Nuev_nodo)

    return distancias



grafo_pequeno = [
    [0, 5, 1],
    [5, 0, 2],
    [1, 2, 0]
]

print(Dijkstra(grafo_pequeno, 0))

grafo_normal = [
    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0]
]

print(Dijkstra(grafo_normal, 0))

