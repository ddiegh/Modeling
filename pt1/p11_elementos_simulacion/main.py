import modelos
from numpy.random import seed, binomial
import matplotlib.pyplot as plt



def main():
    #generar numeros con distribucion binomial 
    seed(42)
    prueba1 = modelos.parcial(binomial(7, 0.8, 200))
    prueba2 = modelos.parcial(binomial(7, 0.8, 200))
    prueba3 = modelos.parcial(binomial(7, 0.8, 200))

    fig, axs = plt.subplots(3, figsize = (10, 8))
    fig.suptitle("Ley de los grandes numeros")

    axs[0].plot(range(200), prueba1)
    axs[1].plot(range(200), prueba2)
    axs[2].plot(range(200), prueba3)

    axs[0].axhline(7*0.8, label = 'Esperanza', c = 'red')
    axs[1].axhline(7*0.8, c = 'r')
    axs[2].axhline(7*0.8, c = 'r')

    axs[0].set_title("Simulación 1")
    axs[1].set_title("Simulación 2")
    axs[2].set_title("Simulación 3")

    fig.legend()
    fig.tight_layout()
    plt.show()

main()