
def falsa_posicion(f, a, b, es):

    if f(a) * f(b) > 0:
        print("Fallo: La función no cambia de signo en el intervalo [a, b]. \n")
        return None

    Xl = a # Extremo izquierdo del intervalo
    Xu = b # Extremo derecho del intervalo

    n = 0 # Contador de iteraciones
    valorPrevio = 0
    raizAproximada = 0
    errorAproximado = 1

    # Mientras el error aproximado sea mayor que el error máximo permitido
    while errorAproximado > es:
        # Calculamos el valor de Xr usando la fórmula de falsa posición
        Xr = Xu - (f(Xu) * (Xl - Xu)) / (f(Xl) - f(Xu))

        fXr = f(Xr) # Evaluo la función en el punto
        raizAproximada = Xr # Guardar la raíz aproximada

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

        # Calculo del error aprox: |(valorActual - valorPrevio) / valorActual| * 100
        errorAproximado = abs((Xr - valorPrevio) / Xr) * 100 
        n += 1 # Incrementar el contador de iteraciones

    print(">> Método de Falsa Posición")
    print("Intervalo inicial: [", a, ",", b, "]")
    print("La aproximación de la raíz es:", raizAproximada)
    print("Con un error aproximado de: ", errorAproximado, "%")
    print("Número de iteraciones: ", n, "\n")
    return

# Probamos el método, primero definimos la funcion
# f(x) = 4x⁴-9x²+14x+1
# Intervalo: [0; 1] 
# Error máximo permitido: 5% ; 0.05

def f(x): # Funcion
    return 4*(x**4) - 9*(x**2) + 14*x + 1

# EJERCICIO 4
# f(x) = (1/(x-1.5))-2
# Intervalo: [1.6; 3] 
def f4(x): # Funcion
    return (1/(x-1.5))-2

falsa_posicion(f, 0, 1, 0.05)

# Elijo este intervalo, para evitar potencialmente el punto 1.5, que daría una división por cero.
falsa_posicion(f4, 1.6, 3, 0.05)
