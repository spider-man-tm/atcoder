import numpy as np

n, k, q = map(int, input().split())
a = []
for _ in range(q):
    a.append(int(input()))

nn = np.zeros(n)
kk = np.zeros(n) + k
qq = np.zeros(n) + q

for i in a:
    nn[i-1] += 1

_list = (kk-qq+nn).tolist()

for ans in _list:
    if ans > 0:
        print('Yes')
    else:
        print('No')