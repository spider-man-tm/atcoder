import numpy as np

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)
cnt = 0
for i in range(N):
    cnt += np.count_nonzero(A[:i]<A[i]) * np.count_nonzero(A[i+1:]<A[i])
print(cnt)