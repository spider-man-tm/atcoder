import numpy as np

N = int(input())
A = sorted(list(map(int, input().split())))
cumsumA = list(np.array(A).cumsum())
sumA = cumsumA[-1]

ans = 0
for i in range(N-1):
    tmp = sumA - cumsumA[i]
    n = A[i] * (N-1-i)
    ans += tmp - n

print(ans)