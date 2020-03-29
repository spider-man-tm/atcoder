import numpy as np

n, m = map(int, input().split())

seikai = np.zeros(n)
matigai1 = np.zeros(n)
matigai2 = np.zeros(n)
for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    if seikai[p]==1:
        continue
    else:
        if s=='AC':
            seikai[p] = 1
            matigai2[p] = matigai1[p]

        else:
            matigai1[p] += 1

print(int(seikai.sum()), int(matigai2.sum()))