# Teorema central del limite y teorema de Glivenko-Cantelli
En esta practica probaremos computacionalmente dos teoremas muy grandes de probabilidad. La idea es probarlos en distintas circunstancias (distribuciones).

## 1. Teorema central del limite 
El TCL nos afirma lo siguiente:

Sean $X_1, X_2, ..., X_n$ variables aleatorias independientes e identicamente distribuidas con esperanza $E(X_i)$ =  $\mu$ y varianza $Var(X_i)$ = $\sigma^2$ entonces
$$Z = \frac{(X_1 + X_2 + ... + X_n) - n \mu}{\sigma \sqrt n} \sim N(0,1)$$

### 1.1 Modelo
Primero creamos una funcion la cual recibe los n valores ($X_i$), la esperanza y la varianza; apartir de eso podemos regresar la nueva variable aleatoria $Z$. 

```python 

def lim_central(X:list, m: float, s: float):
    return Z

```
Una vez que tenemos la nueva variable aleatoria, vamos a generar una cantidad grande de ellas y ver como se distribuyen usando un histograma. 

### 1.2 Simulaciones
El teorema lo probamos con 3 distribuciones que creamos de cero en la practica pasada (se encuentran en `distribuciones.py`): 
* Uniforme(0, 1)
* Exp(2)
* Pareto($\alpha = 2$, c=1 )

Usaremos 50,000 variables aleatorias $X_i$ en cada distribucion, luego generaremos al rededor de 2000 numeros con esa distribucion $Z$ para ver la distribucion.


####  Uniforme(0, 1)
![Unif](imagenes%20/Figure_1.png)

#### Exp($\lambda = 2$ )
![exp](imagenes%20/Figure_2.png)

#### Pareto($\alpha = 3$, c = 1)
![pareto](imagenes%20/Figure_3.png)

Las simulaciones corren muy bien pero con valores arriba de 5000 el tiempo se vuelve muy lento por lo que se vuelve complicado simular muchas variables aleatorias.

