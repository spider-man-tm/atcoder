N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = float('inf')

for i in range(N-K+1):
    start = A[i]
    end = A[i+K-1]

    if start*end>0:
        dist = max(abs(start), abs(end))
    else:
        dist = abs(start)+abs(end)+min(abs(start), abs(end))

    ans = min(ans, dist)

print(ans)