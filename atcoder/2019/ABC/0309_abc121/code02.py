import numpy as np

n, m, c = map(int, input().split())
b = np.array(list(map(int, input().split())))
ans = 0
for _ in range(n):
    a = np.array(list(map(int, input().split())))
    if sum(a*b)+c > 0:
        ans += 1

print(ans)