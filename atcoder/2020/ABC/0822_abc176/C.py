N = int(input())
A = list(map(int, input().split()))

cnt = 0
prv = 0

for i in range(N):
    now = A[i]
    if prv > now:
        cnt += prv - now
    else:
        prv = now

print(cnt)