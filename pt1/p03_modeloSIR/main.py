import matplotlib.pyplot as plt
from modelos import Sistema, R_o

def main():
    caso1 = [1000000, 127, 0, 1, 0.6, 150]
    caso2 = [100000, 200000, 0, 0.7, 0.5, 150]
    caso3 = [200000, 1000000, 0, 0.75, 0.5, 150]
    caso4 = [1000000, 10, 0, 0.75, 0.5, 100]
    # [So, Io, Ro, alfa, beta, iteraciones]

    casos = [caso1, caso2, caso3, caso4]

    for caso in casos:
        So, Io, Ro, alfa, beta, iteraciones = caso

        N = Io + Ro + So
        r0_valor = R_o(alfa, So, N, beta)

        x = range(iteraciones + 1)
        S, I, R = Sistema(So, Io, Ro, alfa, beta, iteraciones)

        plt.figure(figsize=(12, 7))
        plt.plot(x, S, color='blue',  label='Susceptibles')
        plt.plot(x, I, color='red', label = 'Infectados')
        plt.plot(x, R, color='green', label = 'Recuperados')
        plt.legend(loc='upper right', fontsize=12)
        plt.text(
            100, 250000, f'$R_0 = {r0_valor:.2f}$')
        plt.title('Dinámica del Modelo Epidemiológico SIR', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Tiempo (días)', fontsize=13)
        plt.ylabel('Número de Individuos', fontsize=13)
        plt.tight_layout()
        plt.show()


main()
        


