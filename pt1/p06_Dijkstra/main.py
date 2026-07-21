### En este archivo probamos las funciones de Dijkstra con tres matrices de pesos las cuales
#  representan distintos grafos

from modelos import dijkstra, mostrar_rutas, distancia_puntos

#definimos las matrices
M1 = [
    [0, 3, 0, 2, 0, 0, 0, 0],
    [3, 0, 1, 0, 4, 0, 0, 0],
    [0, 1, 0, 3, 0, 2, 2, 0],
    [2, 0, 3, 0, 0, 0, 4, 0],
    [0, 4, 0, 0, 0, 0, 0, 6],
    [0, 0, 2, 0, 0, 0, 3, 4],
    [0, 0, 2, 4, 0, 3, 0, 5],
    [0, 0, 0, 0, 6, 4, 5, 0]
]


M2 = [
    [0, 9, 0, 6],
    [0, 0, 0, 1],
    [0, 3, 0, 0],
    [0, 0, 2, 0]
]

M3 = [
    [0, 4, 8, 16],
    [0, 0, 5, 11],
    [0, 0, 0, 6],
    [0, 0, 0, 0]
]


def main():
    matrices = [M1, M2, M3]

    for matriz in matrices:
        print("----"*30)
        mostrar_rutas(matriz, 0)


if __name__ == "__main__":
    main()




