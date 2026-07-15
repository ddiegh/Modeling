import matplotlib.pyplot as plt
from modelos import rls
from numpy import linspace

longitudes = [36.81, 31.77, 43.82, 36.82, 32.07, 45.07, 35.89]
masas = [0.78, 0.47, 1.16, 0.74, 0.44, 1.40, 0.64]
circunferencias_max = [24.77, 21.29, 27.94, 24.77, 21.59, 31.75, 22.86]
gravity = 9.81


def ejercicio1():
    #relacion que buscamos
    ejes_x = [l**3 for l in longitudes]
    ejes_y = [masa*gravity for masa in masas]

    plt.figure(figsize=(9,7))
    plt.scatter(ejes_x, ejes_y, color='blue')
    plt.xlabel("l^3")
    plt.ylabel("W=mg")
    plt.title("Comparación entre W y l**3")
    plt.legend()
    plt.show()

    return ejes_x, ejes_y

def ejercicio2():
    #ocupamos los datos del ejercicio pasado
    ejes_x, ejes_y = ejercicio1()

    #hacemos una regresion lineal 
    b, m = rls(ejes_x, ejes_y)

    x = linspace(min(ejes_x), max(ejes_x))
    y1 = m*x

    plt.figure(figsize=(9, 7))
    plt.scatter(ejes_x, ejes_y, color='blue',label = 'W=mg' )
    plt.plot(x, y1, label = "recta W = Kl^3", color = 'red')
    plt.xlabel("l^3")
    plt.ylabel("Valores")
    plt.legend()
    plt.show()



def ejercicio3():
    ejex = [l*c**2 for l, c in zip(longitudes, circunferencias_max)]
    ejes_y = [masa*gravity for masa in masas]

    b, m = rls(ejex, ejes_y)
    x = linspace(min(ejex), max(ejex))
    y = m*x 

    plt.figure(figsize=(9,7))
    plt.scatter(ejex, ejes_y, color = 'blue', label = "W = mg")
    plt.plot(x, y, label = 'recta W = k(lC^2)', color = 'red')
    plt.xlabel("l*C^2")
    plt.title("Modelo usando circunferencia")

    plt.show()




def main():
    ejercicio2()
    ejercicio3()

if __name__ == "__main__":
    main()