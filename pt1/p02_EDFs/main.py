import matplotlib.pyplot as plt 
from numpy import linspace
import modelos as modelo

def ej1():

    k_valores = [2, 1, 0.5, -0.5, -1, -2]
    x = range(50)

    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    ejes = axs.flatten()

    for i, k in enumerate(k_valores):
        datos_y = modelo.crec_exp(k)
        ejes[i].scatter(x, datos_y, s=10, color='red')
        ejes[i].plot(x, datos_y, color='blue', linewidth=1)
        ejes[i].set_title(f'comportamiento con k={k}')
        ejes[i].grid(True)

    plt.tight_layout()
    plt.show()


def ej2():
    valores_iniciales = [5, 1000, 1500]
    x = range(41)
    fig, axs = plt.subplots(3, figsize=(10, 12), sharex=True, sharey=True)

    for i, j in enumerate(valores_iniciales):
        datos_y = modelo.logistica(j)
        axs[i].scatter(x, datos_y, color = 'red')
        axs[i].plot(x, datos_y, color='blue')
        axs[i].set_title(f'comportamiento con el valor inicial {j}')
        axs[i].grid(True)
    
    plt.tight_layout()
    plt.show()

# Ejercicio 3
def ej3():
    x = list(range(21))
    r = [0.5, 1, 1, 2]
    b = [2, 1, 0, 2]

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    ejes = axs.flatten()

    for i in range(len(r)):
        valores = modelo.lineal(r[i], b[i])
        ejes[i].scatter(x, valores, c='red')
        ejes[i].plot(x, valores, c='black')
        ejes[i].set_title(f'comportamiento con r={r[i]} y b={b[i]}')
        ejes[i].grid()

    plt.tight_layout()
    plt.show()

def ej4():
    deltas = [0.5, 1, 5, 20]

    fig, axs = plt.subplots(2, 2, figsize = (12, 8))
    ejes = axs.flatten()

    for i, delta in enumerate(deltas):
        y_dis = modelo.sol_DF(delta)

        x_dis = [t * delta for t in range(20)]

        x_cont = linspace(0, max(x_dis), 100) 
        y_cont = modelo.solucion(x_cont)     
        
        ejes[i].scatter(x_dis, y_dis, color='red', label='Aprox. Numérica')
        ejes[i].plot(x_cont, y_cont, color='blue', label='Sol. Analítica')
        
        ejes[i].set_title(f'Delta x = {delta}')
        ejes[i].legend()

    plt.tight_layout()
    plt.show()

def main():
    ej1()
    ej2()
    ej3()
    ej4()

if __name__ == "__main__":
    main()