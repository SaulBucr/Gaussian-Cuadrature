import numpy as np

def gaussxw(N):
    """Crea un array con los puntos de muestreo y los pesos
    
    Examples:
        >>> gaussxw(3)
	(array([-0.77459667,  0.        ,  0.77459667]), 
        array([0.55555556, 0.88888889, 0.55555556]))

    Args:

	N (int): Número de puntos utilizados para la cuadratura Gaussiana

    Returns:
        tuple: Contiene una tupla con los puntos de muestreo y sus pesos

    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """Escala los puntos y pesos de la cuadratura al intervalo de integración 
    
    Examples:
	>>> gaussxwab(1, 2, gaussxw(2)[0], gaussxw(2)[1])
        (array([1.21132487, 1.78867513]), array([0.5, 0.5]))

    Args:
       a (int): límite inferior del intervalo de integración
       b (int): límite superior del intervalo de integración
       x (np.array): Array que contiene los puntos de muestreo
       w (np.array): Array que contiene los pesos

    Returns:
       tuple: Contiene dos arrays de NumPy con los puntos y pesos escalados al intervalo elegido (a, b).
 
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def funcInt(varInd):
    """Evalúa la función que se desea integrar
    
    Examples:
       >>> funcInt(1.0)
       0.090702573
    
    Args:
      varInd (float): variable independiente de la función

    Returns:
      float: Devuelve el valor del argumento varInd evaluado en la función

    """
    factSin = 2 * varInd
    return varInd ** 6 - (varInd**2) * np.sin(factSin)
