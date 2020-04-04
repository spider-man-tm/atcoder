import numpy as np
import math

N = int(input())

c = np.zeros((10, 10), dtype=int)
d = np.zeros((10, 10), dtype=int)

for n in range(1, N+1):
    k = math.floor(math.log10(n)) + 1
    #print('桁数: ', k)
    i = n// (10 ** (k-1))
    #print('1番大きな桁の数: ', i)
    j = n%10
    #print('1の位の数: ', j)
    c[i][j] += 1
    d[j][i] += 1

ans = np.sum(c*d)
print(ans)