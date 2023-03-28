def contar_digitos(num):
    if num < 10:
        return 1
    else:
        return 1 + contar_digitos(num // 10)


print(contar_digitos(123456))


