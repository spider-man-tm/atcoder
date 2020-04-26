N, M = map(int, input().split())
A = list(map(int, input().split()))

if N>=sum(A):
    print(N-sum(A))
else:
    print(-1)