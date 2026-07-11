import matplotlib.pyplot as plt 
from modelos import sistema

def graficas(t, Cn, Zn, a, b):
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))

    axs[0].plot(t, Cn, c='green')
    axs[0].set_title('Conejos a través del tiempo')
    axs[0].set_xlabel('Tiempo (t)')
    axs[0].set_ylabel('Conejos ($C_n$)')

    axs[1].plot(t, Zn, c='orange')
    axs[1].set_title('Zorros a través del tiempo')
    axs[1].set_xlabel('Tiempo (t)')
    axs[1].set_ylabel('Zorros ($Z_n$)')

    axs[2].plot(Cn, Zn, c='blue')
    axs[2].set_title('Retrato de fase')
    axs[2].set_xlabel('Conejos ($C_n$)')
    axs[2].set_ylabel('Zorros ($Z_n$)')
    axs[2].scatter(a, b, c='red', label='punto de equilibrio')
    axs[2].legend()

    plt.tight_layout()
    plt.show()

def main():
    v1 = [0.2, 0.9, 0.08, 0.1, 0.01, 0.15, 100]
    v2 = [0.2, 0.5, 0.25, 1.8, 0.91, 0.6, 1000]
    v3 = [0.2, 0.5, 0.25, 1.1, 0.95, 0.55, 300]

    for v in [v1, v2, v3]:
        tiempos, cn, zn, a, b = sistema(*v)
        graficas(tiempos, cn, zn, a, b)


if __name__ == "__main__":
    main()

