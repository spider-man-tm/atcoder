N, M = map(int, input().split())
A = list(map(int, input().split()))
to = sum(A)
cnt = 0
for a in A:
    if a>=(to * (1/(4*M))):
        cnt += 1

if cnt >= M:
    print('Yes')
else:
    print('No')