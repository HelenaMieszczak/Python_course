
a = int(input("podaj liczbę:"))
b = int(input("podaj liczbę "))


def nwd(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a


print((nwd(a, b)))


def nww(a, b):
    nww = a*b/nwd(a,b)
    return nww

print(nww(a, b))