N = int(input())
a = list(map(int, input().split()))

from math import gcd   # gcd(6, 4) -> 2
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)


print(gcd_list(a))