import modelos
import numpy as np
import matplotlib.pyplot as plt


P1 = np.array([[0.5, 0.5, 0], 
                [0.5, 0, 0.5],
                [0, 0.5, 0.5]])

P2 = np.array([[0.5, 0.5, 0], 
                [0.5,99/200, 1/200], 
                [0, 0, 1]])


P3 = np.array([
    [0, 1, 0, 0, 0, 0],
    [1/5, 0, 4/5, 0, 0, 0],
    [0, 2/5, 0, 3/5, 0, 0],
    [0, 0, 3/5, 0, 2/5, 0],
    [0, 0, 0, 4/5, 0, 1/5],
    [0, 0, 0, 0, 1, 0]
])

P4 = np.array([
    [1, 0, 0, 0, 0, 0],
    [0.5, 0, 0.5, 0, 0, 0],
    [0, 0.5, 0, 0.5, 0, 0],
    [0, 0, 0.5, 0, 0.5, 0],
    [0, 0, 0, 0.5, 0, 0.5],
    [0, 0, 0, 0, 0, 1]
])


def main():
    matrices = [P1, P2, P3, P4]
    cantidad_estados = [3, 3, 6, 6]

    for n, P in zip(cantidad_estados, matrices):  
        Pi_0 = np.random.random(n)
        Pi_0 /= Pi_0.sum()

        prueba = modelos.cadena_markov_recorrido(P, Pi_0)
        plt.figure(figsize=(10, 8))
        plt.step(range(101),prueba)
        plt.xlabel('Tiempo')
        plt.ylabel('Estado')
        plt.title(f'Pasos que toma la cadena')
        plt.legend()
        plt.show()

        P_n = np.linalg.matrix_power(P, 1000)

        proba = np.dot(Pi_0, P_n)

        print(f"las probas de cada estado en el paso 1000 son: {proba}")


if __name__ == "__main__":
    main()