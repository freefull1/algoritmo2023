def calcular_serie(n):
    if n == 1:
        return 1
    else:
        return 1/n + calcular_serie(n-1)

n = 5
resultado = calcular_serie(n)
print("La suma de la serie hasta", n, "es:", resultado)
