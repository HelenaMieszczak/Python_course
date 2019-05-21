# Napisz program, który wyświetli kolejne wyniki dla silnii liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

num = int(input("Podaj dowolną cyfrę (1 - 8): "))

N = 1

for i in range(1, num + 1):
    N *= i
    print(i, "! =", N)
