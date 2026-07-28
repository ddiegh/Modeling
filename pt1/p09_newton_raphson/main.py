from numpy import linspace
import matplotlib.pyplot as plt 
from modelos import newton_raphson, punto_fijo

def f(x):
    return 2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1

def df(x):
    return 8*x**3 + 72*x**2 + 122*x - 16

def g1(x):
    return (2*x**4 + 24*x**3 + 61*x**2 + 1) / 16

def g2(x):
    return -1 / (2*x**3 + 24*x**2 + 61*x - 16)
    
def main():
    #definimos la funcion que nos interesa, sus derivadas y las funciones g1 y g2 


    # grafica de f
    x = linspace(0.12, 0.125, 200)
    fig, ax = plt.subplots()
    ax.plot(x, f(x), label = 'Funcion del ejercicio')
    ax.axhline(0, c = 'gray')
    plt.legend()
    plt.show()

    #probamos newton-raphson y punto fijo con los mismos puntos 
    xo = [0.1213, 0.1231, 0.122, 0.118]
    
    for x in xo:
        print("-"*30)
        print("-"*30)
        print("-"*30)
        sim1 = newton_raphson(f, df, x, 1e-10, 10000)
        sim2 = punto_fijo(x, g1, 1e-10, 10000)
        sim3 = punto_fijo(x, g2, 1e-10, 10000)

        print(f" punto inicial {x}")
        print(f"numero de iteraciones con Newton-Raphson: {len(sim1)}")
        print(f"valor en el ultimo punto {f(sim1[-1])}")

        print("-"*30)
        print(f"numero de iteraciones con punto fijo y g1 {len(sim2)}")
        print(f"valor del ultimo punto {sim2[-1]}")
        print(f"g1 aplicada en el punto fijo {g1(sim2[-1])}")

        print("-"*30)
        print(f"numero de iteraciones con punto fijo y g2 {len(sim3)}")
        print(f"valor en el ultimo punto {sim3[-1]} ")
        print(f"g2 aplicada en el punto fijo: {g2(sim3[-1])}")

if __name__ == "__main__":
    main()