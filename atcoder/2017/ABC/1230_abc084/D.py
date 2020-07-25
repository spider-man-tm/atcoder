import numpy as np
from bisect import bisect_left, bisect_right


def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2, N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


sosu = seachPrimeNum(10**5)[1:]
like_2017 = [i for i in sosu if is_prime((i+1) / 2)]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l_ix = bisect_left(like_2017, l)
    r_ix = bisect_right(like_2017, r)
    print(r_ix - l_ix)
