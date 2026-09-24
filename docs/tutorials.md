## Cálculo de la integral 
Se va a calcular
 
$$
\int_{1}^{3} \left( x^6 - x^2 \sin(2x) \right) \, dx
$$
 
Utilizando un $N = 4$ y un $N = 5$.
 
```
import gaussian
from gaussian import gaussxw, gaussxwab, funcInt
import numpy as np
 
x_w_4 = gaussxw(4)
x_w_5 = gaussxw(5)

``` 
Cada uno devuelve una tupla con dos arrays correspondientes a los puntos Gaussianos $x_k$ y los pesos $w_k$. Esto para el intervalo de $-1$ a $1$.
 
```
escx_w_4 = gaussxwab(1, 3, x_w_4[0], x_w_4[1])
escx_w_5 = gaussxwab(1, 3, x_w_5[0], x_w_5[1])
```
 
Ahora, se transforman al intervalo de $1$ a $3$, `gausswxab()` se encarga de esto.
 
Finalmente se imprime el resultado
 
```
resultado_4 = np.sum(funcInt(escx_w_4[0]) * escx_w_4[1])
resultado_5 = np.sum(funcInt(escx_w_5[0]) * escx_w_5[1])
 
print(resultado_4)
print(resultado_5)
``` 
