def invertir_entero(num, invertido=0):
    if num == 0:
        return invertido
    else:
        invertido = (invertido * 10) + (num % 10)
        return invertir_entero(num // 10, invertido)


print(invertir_entero(2354))