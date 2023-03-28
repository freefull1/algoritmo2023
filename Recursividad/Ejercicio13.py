def euclides_mcd(a, b):
    if b == 0:
        return a
    else:
        return euclides_mcd(b, a % b)

def euclides_mcm(a, b):
    return abs(a*b) // euclides_mcd(a, b)

a = 24
b = 36
print("El MCM de", a, "y", b, "es:", euclides_mcm(a, b))
