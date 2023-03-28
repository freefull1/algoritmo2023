def sucesion_geometrica(a1, r, n):
    if n == 1:
        return a1
    else:
        an_1 = sucesion_geometrica(a1, r, n-1)
        an = a1 * (r ** (n-1))
        print(an)
        return an

a1 = 2
r = -3
n = 5

print("La sucesión geométrica es:")

sucesion_geometrica(a1, r, n)
