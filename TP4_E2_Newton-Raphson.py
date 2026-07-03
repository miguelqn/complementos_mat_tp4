
import math

# f es la funcion, df es la derivada de la funcion, 
# x0 es la aproximacion inicial, 
# es es el error maximo permitido
def newton_raphson(f, df, x0, es):

    Xi = x0 # Aproximación inicial
    n = 0 # Contador de iteraciones
    raizAproximada = 0 # Variable para almacenar la raíz aproximada
    errorAproximado = 1
    valorPrevio = 0

    # Se itera hasta que el error aproximado sea menor al error máximo permitido
    while errorAproximado >= es: 
        
        # Antes debería verificar si existe la derivada en el punto... Lo dejo para después.

        # Verifico que no sea un punto critico, para evitar la division por cero
        if df(Xi) == 0:
            print("Error: Punto crítico encontrado. \n")
            return None
        
        # Resguardo el valor de Xi
        valorPrevio = Xi
        # Calculo el nuevo valor de Xi
        Xi = Xi - f(Xi) / df(Xi)

        #raizAproximada = f(Xi)
        raizAproximada = Xi

        n += 1
        
        if n > 1:
            errorAproximado = abs((Xi - valorPrevio) / Xi) * 100

    print(">> Método de Newton-Raphson")
    print("Valor inicial: ", x0)
    print("La aproximación de la raíz es:", raizAproximada)
    print("Con un error aproximado de: ", errorAproximado, "%")
    print("Número de iteraciones: ", n, "\n")

    return

# Probamos el método, primero definimos las funciones y su derivada
# f(x) = X³-7x²+14x-6 = 0
# f'(x) = 3x²-14x+14
# Intervalo: [2.7; 3.2] Esto para probarlo en Bisección
# Error máximo permitido: 8% ; 0.08

def f(x): # Funcion
    return (x**3) - 7*(x**2) + 14*x - 6

def dfx(x): # Derivada de la funcion
    return 3*(x**2) - 14*x + 14

# EJERCICIO 4
# f(x) = (1/(x-1.5))-2
def f2(x): # Funcion
    return (1/(x-1.5))-2

def dfx2(x): # Derivada de la funcion
    return -1/(x-1.5)**2

# Pruebo con los valores de los intervalos como Xi, tiene 2 raíces, los dos puntos se acercan a cada una de ellas.
newton_raphson(f, dfx, 2.7, 0.08)
newton_raphson(f, dfx, 3.2, 0.08)

# Ejercicio 4
newton_raphson(f2, dfx2, 4, 0.08)
# Funciona bien entre 1.6 y 2.4, con valores > 2.5 da un error de fuera de rango.
# Esto para el primer cuadrante, que fue lo que se pidió en la consigna.
 
