## Cuadratura Gaussiana

Debido a la complejidad de los sistemas de análisis y la amplitud del rango de la física, no es poco común el encontrarse con integrales para las cuáles un método analítico resulta inconveniente. Naturalmente, existen métodos de aproximación para dichas integrales que permiten la obtención de un valor numérico. Un método de esta naturaleza es el de la cuadratura Gaussiana, a utilizar en este programa.
 
## Cuadratura Gaussiana

La cuadratura Gaussiana es un método que se utiliza para aproximar el valor numérico de una integral en un intervalo ya sea de [-1, 1], o en intervalos arbitrarios, mediante una suma ponderada.

La aproximación está dada de la siguiente manera:

$$
\begin{align}
\int_a^b {\rm{d}}x f(x) \approx \sum_{k=1}^{N} w_k f(x_k).
\end{align}
$$

donde:
  * $w_k$ son los "pesos"
  * $x_k$ son los puntos de muestreo

N representa la cantidad de puntos de muestreo utilizados en la cuadratura Gaussiana, y es exacta hasta un polinomio de orden $(2N - 1)$

Los puntos de muestreo $x_k$ corresponden a los ceros de los polinomios de Legendre $P_N(x)$ de orden $N$.

En cuanto a los pesos, estos se eligen tal que:

\[
 w_k = \left[ \frac{2}{1-x^2} \left( \frac{dP_N}{dx} \right)^{-2} \right]_{x={x_k}} 
\]

## Objetivo del módulo

El siguiente programa de Python busca la resolución de una integral por medio del método de cuadratura Gaussiana.

Primeramente, se obtienen los puntos de muestreo y los pesos correspondientes a la cantidad de puntos $N$ utilizada. Estos puntos y pesos se encuentran inicialmente definidos para el intervalo $[-1,1]$. Por medio de una transformación, estos valores pueden ser adaptados a un intervalo arbitrario de integración.

La función que se busca integrar por medio de esta metodología corresponde a:

$$f(x) = x^6 - x^2 \sin(2x)$$

En este caso, se utiliza el intervalo de $[1, 3]$. Por ende, la integral a aproximar es:

$$\int_{1}^{3} \left( x^6 - x^2 \sin(2x) \right) \, dx$$

