import numpy as np
import fractions
from functools import reduce

N, X = map(int, input().split())
x = list(map(int, input().split()))
x = np.array(x)

x -= X
x = abs(x)
x = x.tolist()

def gcd(numbers):
    return reduce(fractions.gcd, numbers)

print(gcd(x))