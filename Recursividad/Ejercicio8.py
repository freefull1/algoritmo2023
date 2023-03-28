def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'
    elif decimal == 1:
        return '1'
    else:
        cociente = decimal // 2
        resto = decimal % 2
        return decimal_a_binario(cociente) + str(resto)
    
print(decimal_a_binario(32000))