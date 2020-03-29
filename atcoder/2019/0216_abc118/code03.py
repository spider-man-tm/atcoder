import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)


n = int(input())
a = list(map(int, input().split()))

print(gcd_list(a))