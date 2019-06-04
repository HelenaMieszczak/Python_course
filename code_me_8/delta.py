# Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.

import math


def count_delta(a, b, c):
    d = pow(b, 2) - 4 * a * c
    return d


def check_delta(d):
    if d < 0:
        return False
    else:
        return True
