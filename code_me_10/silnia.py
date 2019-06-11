# Przypomnij sobie szkolny wzór na silnię. Zapisz funkcję silnia iteracyjnie np. pętlą for,
# a następnie analogiczną funkcję tylko, że rekurencyjnie.


def silnia_for():
    num = int(input("Podaj dowolną cyfrę: "))
    N = 1
    for i in range(1, num + 1):
        N *= i
        print(i, "! =", N)


silnia_for()
print("*****")

num_r = int(input("Podaj dowolną cyfrę: "))


def silnia_rekurencyjnie(num_r):
    if num_r == 1:
        return 1
    else:
        return num_r * silnia_rekurencyjnie(num_r - 1)


print(silnia_rekurencyjnie(num_r))
