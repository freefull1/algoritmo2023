def mcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return mcd(b, r)



print(mcd(17, 5)) 
