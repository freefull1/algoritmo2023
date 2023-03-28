def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)
print(calcular_potencia(2,2))