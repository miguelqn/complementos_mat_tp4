import math

# f es la funcion, a y b son los extremos del intervalo cerrado, es el limite del error aproximado para detener el proceso iterativo, e.g. 0.01
# Luego que corte con el error, e iteraciones libres, si llega a e=0.08
def biseccion(f, a, b, es):

    if f(a) * f(b) > 0: # Verificar que la función cambia de signo en el intervalo
        print("Fallo: La función no cambia de signo en el intervalo [a, b]. \n")
        return None
    
    Xl = a # Extremo izquierdo del intervalo
    Xu = b # Extremo derecho del intervalo

    n = 0 # Contador de iteraciones
    valorPrevio = 0
    raizAproximada = 0
    errorAproximado = 1

    while errorAproximado > es: # Mientras el error aproximado sea mayor que el error máximo permitido
        Xr = (Xl + Xu) / 2 # El punto medio del intervalo
        fXr = f(Xr) # Evaluar la función en el punto medio

        if f(Xl) * fXr < 0: # Si el producto es negativo, la raíz está en [Xl, Xr]
            valorPrevio = Xu
            Xu = Xr
        elif f(Xl) * fXr > 0: # Si el producto es positivo, la raíz está en [Xr, Xu]
            valorPrevio = Xl
            Xl = Xr
        elif fXr == 0:
            print("La solución exacta es:", Xr, "\n")
            return
        else:
            print("Error: No se pudo determinar la raíz. \n")
            return
        
        raizAproximada = Xr # Guardar la raíz aproximada
        # Calculo del error aprox: |(valorActual - valorPrevio) / valorActual| * 100
        errorAproximado = abs((Xr - valorPrevio) / Xr) * 100 
        n += 1 # Incrementar el contador de iteraciones


    print(">> Método de Bisección")
    print("Intervalo inicial: [", a, ",", b, "]")
    print("La aproximación de la raíz es:", raizAproximada)
    print("Con un error aproximado de: ", errorAproximado, "%")
    print("Número de iteraciones: ", n, "\n")
    return

# EJERCICIO 1
# Probamos las funciones
# Función: x²-x-1
# Intervalo cerrado [0, 2]
# Error máximo permitido: 8% ; 0.08
# Iteraciones esperadas: 5

def funcion1(x): # Funcion dada en el ejercicio 1
    return (x**2) - x -1

# EJERCICIO 2
# f(x) = X³-7x²+14x-6 = 0
# Intervalo: [2.7; 3.2]
def funcion2(x): # Funcion
    return (x**3) - 7*(x**2) + 14*x - 6

# EJERCICIO 4
# f(x) = (1/(x-1.5))-2
# Intervalo: [1.6; 3] 
def funcion3(x): # Funcion
    return (1/(x-1.5))-2

biseccion(funcion1, 0, 2, 0.08)
biseccion(funcion2, 2.7, 3.2, 0.08)
# Elijo este intervalo, para evitar potencialmente el punto 1.5, que daría una división por cero.
biseccion(funcion3, 1.6, 3, 0.08)
