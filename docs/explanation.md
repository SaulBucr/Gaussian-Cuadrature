## Método numérico

La cuadratura Gaussiana está basada en:

$$\int_{-1}^{1} f(x)\,dx \approx \sum_{k=1}^{N} w_k f(x_k),
$$

en donde $x_k$ (puntos de cuadratura) son las raíces de los polinomios de Legendre $P_N(x)$ y $w_k$ sus pesos correspondientes.

Para obtener estos coeficientes, se hace uso de la función `gaussxw(N)`, la cual hace uso de `leggauss(N)`, que provee precisamente los puntos de cuadratura y los pesos correspondientes para ese $N$.

Ahora bien, estos puntos obtenidos en la función `gaussxw()` están definidos en un intervalo de $-1$ a $1$, pero la integral final que se busca viene definida desde $1$ hasta $3$. Por ende, es necesario transformar estos puntos y pesos al intervalo deseado.

Comenzando desde el cambio de variables:

$$
x = \frac{b-a}{2}z + \frac{b+a}{2},
$$

donde $z$ va desde $[-1,1]$ y $x$ va desde $[a,b]$.

El diferencial de la sustitución queda como:

$$
dx = \frac{b-a}{2}\,dz.
$$

Por ende, la integral de $f(x)$ en el intervalo $[a,b]$ queda expresada como:

$$
\int_a^b f(x)\,dx
=
\frac{b-a}{2}
\int_{-1}^{1}
f\left(
\frac{b-a}{2}z + \frac{b+a}{2}
\right)\,dz.
$$

Y finalmente, al aplicar la cuadratura Gaussiana a la integral de $[-1,1]$:

$$
\int_a^b f(x)\,dx
\approx
\frac{b-a}{2}
\sum_{k=1}^{N}
w_k
f\left(
\frac{b-a}{2}x_k + \frac{b+a}{2}
\right).
$$

De donde es evidente el porqué del retorno de la función `gaussxwab()` para el reescalado de los puntos Gaussianos y los pesos. La primera expresión transforma los puntos de cuadratura al intervalo $[a,b]$, mientras que la segunda incorpora el factor $(b-a)/2$ a los pesos.

Seguidamente, la función `funcInt(varInd)` representa la función:

$$f(x) = x^6 - x^2\sin(2x),
$$

siendo esta la función presente en la integrar, editable por otras funcioens según la integrar a resolver. Finalmente, se evalúan los puntos transformados, multiplicándose por los pesos correspondientes, y una sumatoria de NumPy se encarga de ir añadiendo todos estos valores.

