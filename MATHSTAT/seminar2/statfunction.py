# import numpy as np
from math import factorial, pow


def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def aarangements(n, k):
    return factorial(n) // factorial(n-k)

def bernuli(n, k, p):
    return combinations(n, k)*pow(p, k)* pow(1 - p, n-k)

def poison(m, n, p):
    return (pow(n*p, m)/factorial(m))*pow(2.71828,-n*p)
