#  Modelos de Ecuaciones en Diferencias Finitas 

## Introducción
En esta practica se introducen las ecuaciones en diferencias finitas, las cuales son funciones recursivas que nos sirven para resolver ecuaciones diferenciales de forma computacional (metodo de euler)

 Se hacen distintas pruebas con 3 modelos, cambiando algunos parametros para ver como se comportan los sistemas, despues se hace una comparación entre las soluciones analiticas de una EDO y la aproximación numerica.

 ## Estructura de la practica 
 En el archivo `modelos.py` se definen las funciones que nos van a ayudar en cada ejericico, (se definen las diferencias finitas)

 En `main.py` se hace se ocupan los modelos para encontrar los valores numericos de las ecuaciones en diferencias finitas, y se grafican estos valores numericos.

## Analisis

### 1. Crecimiento exponencial
Primero consideremos la siguiente Ecuación en Diferencias Finitas
$$ P_{n+1} = k P_n $$  
veremos como se comporta consideranto distintos valores de $k$

| k: | 2 | 1 | 0.5 | -0.5 | -1 | -2 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

![crecimiento_exp](/imagenes/Figure_1.png)

En esta imagen podemos observar como se comporta el sistema con los distintos valores que consideremos: 
* K>0: 
el sistema tiene un comportamiento exponencial, tanto exponencial positivo como uno negativo 
* K=0: el sistema se mantiene constante
* K<0: se tiene un moviemiento oscilatorio que puede variar dependiendo del valor, ya sea llegando a converger, explotando o quedandose igual 

### 2. Función logistica 
Ahora probaremos las ecuaciones en diferencias finitas en la función logistica: 
$$\frac{dP}{dt} = rP(1-P/K)$$

con valores iniciales  $r=0.5, k=1000$ y las poblaciones iniciales: 
| Po |
| :---: |
| 5 |
| 1000 |
| 1500 |


Lo que se hizo en este ejericio fue primero resolver la ecuación diferencial mediante las ecuaciones en diferencias, llegando a una forma recursiva facil para computar:

$$ P_{n+1} =P_n +  rP_n(1-P_n/K)$$

Una vez hecho esto definir la función en python sale casi inmediatamente, solo hay que definir la funcion con una variable de entrada que será la condición inicial, las constantes que vamos a ocupar y la cantidad de veces que queremos iterar.

```python
def logistica(Po):
    r = 0.5
    k = 1000
    P = [Po]

    for _ in range(40):
        Pn = P[-1]
        P.append(Pn + (r*Pn * (1-(Pn/k))))
    return P
```

Despues de graficar los resultados con los 3 distintos valores iniciales tenemos el siguiente resultado 

![logistica](/imagenes/Figure_2.png)

En todos los caso vemos que la función converge a valor de $1000$ y esto ocurre porque esa es la capacidad de carga del sistema (punto de equilibrio)

### 3. Sistema lineal 
La ecuación que ahora se considera es: 
$$ X_{n+1} = r X_n + b $$
y se probará con los siguientes valores
| Parámetro $r$ | Parámetro $b$ | 
| :---: | :---: 
| 0.5 | 2 | 
| 1 | 1 |
| 1 | 0 | 
| 2 | 2 | 


Al igual que en los ejercicios anterios, pasar el sistema a python sale de forma natural y solo tenemos que graficar los valores numericos que nos arroja el codigo.
![lineal](/imagenes/Figure_3.png)

En este caso podemos ver como hay casos en el que el sistema explota y otros donde converge.

### 4. Comparación entre una solucion analitica y una numerica
En este ejercicio la idea es comparar las soluciones analiticas y numericas de ls ecuacion diferencial
$$\frac{dy}{dx} = -6x + 3$$
con condicion inicial 
$$ y(0)=2$$
---
Lo primero que se hizo fue resolver la ecuación analiticamente y usando diferencias finitas llegando a los resultados

* Solución analitica
$$ y(x) = -3x^2 + 3x +2 $$

* Solución diferencias finitas 
$$ y_{n+1} = y_n + \Delta x (-6x_n+3) $$

Despues de computar las soluciones, encontrar los valores numericos y graficarlos llegamos a la siguiente grafica, en donde podemos notar que las soluciones numericas tienen un pequeño error pero que soy muy cercanas a las soluciones numericas

![soluciones](/imagenes/Figure_4.png)
