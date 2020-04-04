K, N = map(int, input().split())
A = list(map(int, input().split()))

dist = [0] * (N)
for i in range(N):
    if i != N-1:
        dist[i] = A[i+1] - A[i]
    else:
        dist[i] = K-A[i] + A[0]

print(sum(dist) - max(dist))