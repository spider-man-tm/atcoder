import numpy as np

n = int(input())
x = list(map(int, input().split()))
x = sorted(x)
min = np.inf

for i in range(1, x[-1]+1):
    total = 0
    for j in x:
        total += (j-i)**2
    if total < min:
        min = total

print(min)