def potencia(a, b):
    # Caso base: si el exponente es 0, la potencia es 1
    if b == 0:
        return 1
    # Caso recursivo: calculamos la potencia de a^(b-1) y lo multiplicamos por a
    else:
        return a * potencia(a, b-1)



print(potencia(2,2))