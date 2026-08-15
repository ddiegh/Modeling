from modelos import *
import matplotlib.pyplot as plt
from numpy import linspace

Pi_beta = lambda x : dis_beta(2, 3, x)

def graf1():
    simulacion = metropolis_hastings(3, Pi_beta, 1, 1000)
    x = range(len(simulacion))

    plt.figure()
    plt.plot(x, simulacion)
    plt.xlabel("Iteraciones")
    plt.ylabel("Valor de la muestra X")
    plt.title("Metropolis-Hastings: Trayectoria de Muestreo")
    plt.legend()
    plt.show()

def graf2():

    # Parámetros 
    N = 10000
    burn_in = 1000
    X0 = 0.5 
    r = 0.5  

    # 3 densidades Beta del Ejercicio 1
    parametros_beta = [(5, 1), (1, 3), (2, 2)]
    x_teorico = linspace(0, 1, 200)

    plt.figure(figsize=(15, 5))
    for i, (a, b) in enumerate(parametros_beta):
        
        Pi_beta = lambda x: dis_beta(a, b, x)
        trayectoria_cruda = metropolis_hastings(X0, Pi_beta, r, N)
        #Descartamos los primeros 1000
        muestras_finales = trayectoria_cruda[burn_in:]

        y_teorico = [dis_beta(a, b, x) for x in x_teorico]

        plt.subplot(1, 3, i + 1)
        plt.hist(muestras_finales, bins=40, density=True, label='Muestras MH')
        plt.plot(x_teorico, y_teorico, color='red', linewidth=2, label=f'Teórica Beta({a},{b})') 
        plt.title(f'Beta a={a}, b={b} (r={r})')
        plt.xlim(0, 1)
        plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    graf1()
    graf2()

if __name__ == "__main__":
    main()



