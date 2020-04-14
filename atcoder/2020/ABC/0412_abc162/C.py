from itertools import combinations_with_replacement

from math import gcd   # gcd(6, 4) -> 2
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)


N = int(input())
ans = 0
for i, j, k in combinations_with_replacement(range(1, N+1), 3):
    if i==j==k:
        ans += i
    elif i==j:
        ans += gcd(i, k)*3
    elif j==k:
        ans += gcd(j, i)*3
    elif i==k:
        ans += gcd(i, j)*3
    else:
        ans += gcd_list([i, j, k])*6
print(ans)