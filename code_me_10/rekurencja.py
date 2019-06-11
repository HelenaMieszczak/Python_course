def _print(n):
    if n < 0:
        print("-")
        n -= n
    if n // 10 != 0:
        _print(n//10)

    print(n % 10)


_print(123)

# 1 wypisz -> 123 -> 3
# 2 wypisz -> 12 -> 2
# 3 wypisz -> 1 -> 1