N, K = map(int, input().split())
A = list(map(int, input().split()))

tmp = sum(A[:K])
l = A[0]
ans = tmp

for i in range(1, N-K+1):
    diff = A[i+K-1] - l
    tmp += diff
    ans += tmp
    l = A[i]

print(ans)