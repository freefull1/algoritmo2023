def suma_enteros(n):
    if n == 0:
        return 0
    else:
        return n + suma_enteros(n-1)
print(suma_enteros(5))