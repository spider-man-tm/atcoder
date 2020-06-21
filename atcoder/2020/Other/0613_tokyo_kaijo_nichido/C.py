import numpy as np
from numba import jit
N, K = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype=np.int64)

# 高速化
@jit
def imo(a, n):
    imos = np.zeros(n+1, dtype=np.int64)
    for i in range(n):
        imos[max(0, i-a[i])] += 1
        imos[min(n, i+a[i])+1] -= 1

    # 累計和はnumpyの方が高速
    immo = np.zeros(n+1, dtype=np.int64)
    immo = np.cumsum(imos)

    return immo[:n]


for _ in range(min(K, 41)):
    A = imo(A, N)

print(*A)