N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = [0]*N, [0]*M

total = 0
for i in range(N):
    total += A[i]
    a[i] = total

a = [0] + a

total = 0
for i in range(M):
    total += B[i]
    b[i] = total

b = [0] + b

ans, j = 0, M
for i in range(N+1):
    if a[i] > K:
        break
    while b[j] + a[i] > K:
        j -= 1
    #print(a[i], b[j], i, j)
    ans = max(ans, i + j)

print(ans)