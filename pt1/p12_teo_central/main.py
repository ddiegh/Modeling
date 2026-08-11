import distribuciones as dt
from modelos import lim_central, FD_pareto, FD_exp2, FD_unif, FDe
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


tamanos = [10, 100, 1000]

def sim_teo_Glivenko_Cantelli():
    plt.figure(figsize=(15, 4)) 
    for i, n in enumerate(tamanos):
        U = [dt.uniform(0, 1) for _ in range(n)]
        t_unif = np.linspace(-0.5, 1.5, 300)
        
        y_emp = [FDe(U, t) for t in t_unif]
        y_ana = [FD_unif(t) for t in t_unif]
        
        plt.subplot(1, 3, i + 1)
        plt.plot(t_unif, y_emp, color="teal", label="Empírica")
        plt.plot(t_unif, y_ana, color="red", linestyle="--", label="Analítica")
        plt.title(f"Uniforme (0,1) | n = {n}")
        plt.grid(True, alpha=0.3)
        if i == 0: plt.legend()
    plt.tight_layout()

    plt.figure(figsize=(15, 4)) # Crea una segunda ventana separada
    for i, n in enumerate(tamanos):
        X_exp = [dt.exp(2) for _ in range(n)] # Transformada inversa
        t_exp = np.linspace(0, 3, 300)
        
        y_emp = [FDe(X_exp, t) for t in t_exp]
        y_ana = [FD_exp2(t) for t in t_exp]
        
        plt.subplot(1, 3, i + 1)
        plt.plot(t_exp, y_emp, color="teal", label="Empírica")
        plt.plot(t_exp, y_ana, color="red", linestyle="--", label="Analítica")
        plt.title(f"Exponencial (2) | n = {n}")
        plt.grid(True, alpha=0.3)
        if i == 0: plt.legend()
    plt.tight_layout()


    plt.figure(figsize=(15, 4)) # Crea la tercera ventana
    for i, n in enumerate(tamanos):
        X_pareto = [dt.pareto(3, 2) for _ in range(n)]
        t_pareto = np.linspace(0, 10, 300)
        
        y_emp = [FDe(X_pareto, t) for t in t_pareto]
        y_ana = [FD_pareto(t) for t in t_pareto]
        
        plt.subplot(1, 3, i + 1)
        plt.plot(t_pareto, y_emp, color="teal", label="Empírica")
        plt.plot(t_pareto, y_ana, color="red", linestyle="--", label="Analítica")
        plt.title(f"Pareto (3,2) | n = {n}")
        plt.grid(True, alpha=0.3)
        if i == 0: plt.legend()
    plt.tight_layout()

    # Muestra todas las ventanas creadas al mismo tiempo
    plt.show()

def main():
    sim_teo_central_lim()
    sim_teo_Glivenko_Cantelli()

if __name__ == "__main__":
    main()