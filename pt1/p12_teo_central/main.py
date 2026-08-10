import distribuciones as dt
from modelos import lim_central
import matplotlib.pyplot as plt 
import numpy as np
import scipy.stats as stats


def sim_teo_central_lim():
    #valores para las simulaciones
    distribuciones = ["uniform(0, 1)", "exp(2)", "pareto(1, 3)"]
    esperanzas = [0.5, 0.5, 1.5]
    varianzas = [1/3.464, 0.5, 0.866 ]


    for i, (dist, esp, var) in enumerate(zip(distribuciones, esperanzas, varianzas)):
        Z = []

        for _ in range(2000):
            if i == 0:
                X = [dt.uniform(0, 1) for _ in range(5000)]
                
            elif i == 1:
                X = [dt.exp(2) for _ in range(5000)]

            elif i == 2:
                X = [dt.pareto(1, 3) for _ in range(5000)]

            Z.append(lim_central(X, esp, var))

        plt.figure(figsize=(10, 8))
        plt.hist(Z, bins = 50, density=True, label = 'Z simuladas')
        x = np.linspace(-4, 4, 100)
        plt.plot(x, stats.norm.pdf(x, 0, 1), 'r-', lw=2, label='Normal(0,1) Teórica')

        plt.title(f"Teorema Central del Límite con 5000 VA's con distribucion {dist}")

        plt.legend()
        plt.show()

