# Metodos para minimizar funciones (descenso de gradiente y algoritmo evolutivo)

En esta practica implementamos dos metodos para minimizar funciones $f: R^n \rightarrow R$. 

Primero, implementamos una función que calcula el gradiente en un punto dado (`grad`) usando diferencias centradas. 

Con la función anterior tenemos ya casi todo para implementar el `descenso de gradiente` usando la formula recursiva:

$$X_{n+1} = X_n - a \nabla f(X_n)$$

En donde: 
* $f: R^n \rightarrow R$
* $a$: tasa de aprendizaje 

Por ultimo tenemos un `algoritmo evolutivo` el cual considera un intervalo en el que busca valores. 
La idea es tener un punto fijo $(x,y)$ y generar de forma aleatoria un nuevo numero $(u, v)$ en el intervalo $(x-a, x+a)$ X $(y-a, y+a)$. 

Si $f(u, v)$ < $f(x,y)$ entonces nuestro nuevo numero será $(u, v)$ y sino seguimos generando otro numero. 

De vez en cuando generamos un nuevo numero en todo el intervalo inicial y no en $(x-a, x+a)$ X $(y-a, y+a)$ para evitar quedarnos en minimos locales (esto pasa con una probabilidad pequeña).

## Requerimientos
Se ocupa `random.uniforme` para generar numeros aleatorios. 


