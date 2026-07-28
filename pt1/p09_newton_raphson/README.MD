# Practica 9: Metodos numericos para encontras las raices de una función


## Requisitos

- `numpy.linespace` 
- `matplotlib.pyplot` 


# Introducción:

En esta práctica implementamos dos métodos para encontrar raíces de funciones: el método de **Newton-Raphson** y el **método del punto fijo**. Los aplicamos al polinomio

$$
P(x) = 2x^4 + 24x^3 + 61x^2 - 16x + 1
$$

buscando sus raíces cercanas a $x = 0.1$, y comparamos la eficiencia de los dos métodos.

Nos interesa ver cuántas iteraciones necesita cada método para alcanzar la misma tolerancia y cómo influye el punto inicial en su comportamiento.

### Modelo matemático

**Método de Newton-Raphson.** A partir de una aproximación inicial $x_0$, se refina la raíz mediante:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

**Método del punto fijo.** A partir de $x_0$, se itera una función $g$ construida de forma que $g(x) = x \iff P(x) = 0$:

$$
x_{n+1} = g(x_n)
$$

Para que el método converja, $g$ debe ser contractiva en un intervalo alrededor de la raíz, es decir, debe cumplir $|g'(x)| \le k < 1$.

#### Criterios de paro

Ambos métodos tienen dos criterios de paro: una tolerancia $\varepsilon$ y un número máximo de iteraciones.

| Método | Para cuando |
|--------|-------------|
| Newton-Raphson | $\lvert f(x_n)\rvert < \varepsilon$ |
| Punto fijo | $\lvert g(x_n) - x_n\rvert < \varepsilon$ |

### Funciones de iteración
Para el método del punto fijo se usaron dos funciones  $g_1$ y $g_2$:

$$
g_1(x) = \frac{2x^4 + 24x^3 + 61x^2 + 1}{16}
\qquad
g_2(x) = \frac{-1}{2x^3 + 24x^2 + 61x - 16}
$$

## Ejecución

```bash
1. modelos.py
2. main.py
```

## Uso

Las funciones principales son `newton_raphson` y `punto_fijo`. Cada una recibe la condición inicial, las funciones necesarias, la tolerancia y el máximo de iteraciones, y devuelve una lista con todos los valores de las iteraciones.

```python
sim1 = newton_raphson(f, df, xo, epsilon, max_iter)
sim2 = punto_fijo(xo, g, epsilon, max_iter)
```

| Salida | Descripción |
|--------|-------------|
| `sim1` | Lista con todas las iteraciones de Newton-Raphson. |
| `sim2` | Lista con todas las iteraciones del punto fijo. |

El último elemento de cada lista es la aproximación final a la raíz, y la longitud de la lista indica el número de iteraciones realizadas.

La función `main` prueba ambos métodos con distintos puntos iniciales, una tolerancia de $10^{-10}$ y un máximo de $10{,}000$ iteraciones, e imprime cuántas iteraciones tomó cada método.

## Grafica de la funcion
Primero hicimos una grafica para darnos cuenta en que intervalo podiamos encontrar las raices y asi definir nuestros puntos iniciales.
![imagen 1](/imagenes/Figure_1.png)

## Análisis

Se probaron los dos métodos con cuatro puntos iniciales distintos. La siguiente tabla muestra el número de iteraciones que necesitó cada uno para alcanzar la tolerancia $\varepsilon = 10^{-10}$:

| $x_0$ | Newton-Raphson | Punto fijo $g_1$ | Punto fijo $g_2$ | 
|-------|----------------|------------------|------------------|
| 0.1213 | 3 | 941 | 527 |
| 0.1231 | 3 | 2253 | 1198 |
| 0.122 | 6 | 1451 | 789 |
| 0.118 | 7 | 1457 | 793 |

**Newton-Raphson es mucho más eficiente que el punto fijo.** Mientras que Newton necesita entre 3 y 7 iteraciones, el punto fijo necesita cientos o miles. 

**$g_2$ converge más rápido que $g_1$.** En todos los puntos iniciales, $g_2$ necesita aproximadamente la mitad de iteraciones que $g_1$.

**El punto inicial afecta más al punto fijo que a Newton.** Para Newton el número de iteraciones apenas cambia (de 3 a 7) al alejarse de la raíz, mientras que para el punto fijo el conteo varía mucho (por ejemplo, $g_1$ pasa de 941 a 2253 iteraciones según el punto de arranque).

Además, los valores finales de $|f(x_n)|$ muestran que Newton no solo es más rápido sino que termina con mayor precisión: alcanza valores del orden de $10^{-12}$ a $10^{-16}$, mientras que el punto fijo se queda alrededor de $10^{-9}$, debido a que su criterio de paro mide el cambio entre iteraciones y no directamente el valor de la función.

### Analis de punto fijo
A la hora de analizar los puntos fijos que encontramos y evaluarlos en sus respectivas funciones obtenemos lo siguiente 
|punto inical | punto encontrado en g1 | punto evaluado en g1 |
|-------|----------------|------------------|
|0.1213| 0.12132033084262242 |  0.12132033094188875 |
| 0.1231 | 0.12132035631481083 | 0.12132035621524814 | 
| 0.122 | 0.12132035635709364 | 0.1213203562572009 | 


|punto inical | punto encontrado en g2 | punto evaluado en g2 |
|-------|----------------|------------------|
|0.1213| 0.12132033701729804  |  0.12132033711642735 |
|0.1231| 0.12132035008974494 | 0.12132034999080182 | 
| 0.122| 0.12132035009637607 | 0.12132034999733247 | 

Lo que nos hace darnos una idea de que si está funcionando el algoritmo para encontrar los puntos fijos pues al evaluarlos en la funcion obtenemos lo mismo con un cierto error pequeño. 




## Conclusión

Con esta práctica podemos ver que, aunque ambos métodos llegan a la misma raíz, el método de Newton-Raphson es mucho más eficiente que el método del punto fijo, tanto en número de iteraciones como en precisión final. El punto fijo depende fuertemente de qué tan buena sea la función de iteración $g$ elegida. También se observa que la elección del punto inicial influye más en el punto fijo que en Newton, que se mantiene rápido incluso arrancando lejos de la raíz.
