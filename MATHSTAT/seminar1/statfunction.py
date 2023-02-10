import numpy as np
from math import factorial


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def aarangements(n, k):
    return factorial(n) // factorial(n-k)
