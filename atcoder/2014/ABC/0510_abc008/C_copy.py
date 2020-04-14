from math import floor

N = int(input())
C = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    tmp = C[i]
    p = 0
    for some in C:
        if tmp%some == 0:
            p += 1
    cnt += floor((p+1) / 2) / p

print(cnt)