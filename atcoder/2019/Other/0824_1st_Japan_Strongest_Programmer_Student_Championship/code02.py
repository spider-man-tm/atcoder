N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9+7

q1 = 0
for i in range(N):
    for j in range(i, N):
        if A[i]>A[j]:
            q1 += 1

q2 = 0
for i in range(N):
    for j in range(N):
        if A[i]>A[j]:
            q2 += 1

tmp1 = (K-1)*K//2 %mod * q2 %mod
tmp2 = q1*K%mod
ans = (tmp1 + tmp2)%mod
print(int(ans))