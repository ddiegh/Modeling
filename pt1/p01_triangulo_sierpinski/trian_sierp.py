import matplotlib.pyplot as plt
import random 

#creamos la funcion que nos hará el triangulo de Sierpinski
def puntos(i,j):      #los argumentos son las coordenadas del punto inicial 
    #creamos un tringualo equilatero con vertices A,B,C
    A = (0, 0)
    B = (10, 0)
    C = (5, 8.660)
    
    #ponemos juntos los vertices en un array para despues poder elegir alateoriamete entre ellos
    p = [A,B,C]

    #creamos el algoritmo 
    for _ in range(10000):
        plt.scatter(i,j,s=8)        #dibujamos el punto 
        r = random.choice(p)        #escogemos un verice aleatoriamente 
        #el nuevo punto será el punto medio entre el anterior y el vertice elegido 
        i = (i+r[0])/2              
        j = (j+r[1])/2
        #se repite el algoritmo (10,000 veces)
    
    #graficamos los vertices 
    plt.scatter(0,0,s=8)
    plt.scatter(10,0,s=8)
    plt.scatter(5,8.660,s=8)
    #graficamos el plano final
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    puntos(4,4)   #probamos con el punto inicial (4,4)