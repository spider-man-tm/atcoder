from bisect import bisect_left
from math import ceil

N, H = map(int, input().split())
a, b = [], []

for _ in range(N):
    inp = list(map(int, input().split()))
    a.append(inp[0])
    b.append(inp[1])

Amax = max(a)
b = sorted(b)

ix = bisect_left(b, Amax)
katana = [Amax] + b[ix:]
katana = list(reversed(katana))

if sum(katana) >= H:
    cnt = 0
    for i in range(len(katana)):
        cnt += katana[i]
        if cnt >= H:
            print(i+1)
            exit()

else:
    amari = ceil((H - sum(katana)) / Amax)
    print(amari + len(katana))