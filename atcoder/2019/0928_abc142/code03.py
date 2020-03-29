n = int(input())
a = list(map(int, input().split()))

import numpy as np

a = np.array(a)
arg = a.argsort()

for i in arg:
    print(i+1, end=' ')