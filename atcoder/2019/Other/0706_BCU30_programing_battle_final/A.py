N, K = map(int, input().split())
A = sorted([int(input()) for _ in range(N)], reverse=True)

ans = sum(A[:K]) + 2*sum(A[K:])
print(ans)