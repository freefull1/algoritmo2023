def invertir_secuencia(secuencia):
    if len(secuencia) == 0:
        return ""
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])
print(invertir_secuencia('Hola mundo'))