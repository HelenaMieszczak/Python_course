# Stwórz listę składającą się z kilku elementów różnego typu.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

random_list = ["kot", 5, 0, 85, "aaaa", 1.5]

for thing in random_list:
    print("--------------")
    try:
        print(thing)
        r = thing / 10
        print(r)
        continue
    except (ZeroDivisionError, ValueError, TypeError) as error:
        print(error)


