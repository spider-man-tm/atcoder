from bisect import bisect_left, bisect_right  # return index
from math import ceil, floor

N, H = map(int, input().split())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

amax = max(A)
B = sorted(B)
ix = bisect_right(B, amax)
l = [amax] + B[ix:]
l = list(reversed(l))

if sum(l) > H:
    cnt = 0
    for i in range(len(l)):
        cnt += l[i]
        if cnt >= H:
            print(i + 1)
            exit()
else:
    cnt = len(l)
    amari = H - sum(l)
    cnt += ceil(amari / amax)
    print(cnt)