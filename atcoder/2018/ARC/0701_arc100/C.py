import numpy as np

N = int(input())
A = list(map(int, input().split()))

diff = []
for i in range(N):
    diff.append(A[i] - (i+1))

b = int(np.median(diff))

ans = 0
for i in range(N):
    ans += abs(A[i] - (b + (i+1)))

print(ans)