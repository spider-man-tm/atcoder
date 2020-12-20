N, K = map(int, input().split())

K = abs(K)

# [0,0,1,2,3, ...,2*N,2*N-1,2*N-2, ...,1]
num = [0] * (2*N+1)

for i in range(2, 2*N+1):
    num[i] = min(i-1, 2*N+1-i)

ans = 0
for i in range(K, 2*N+1):
    ans += num[i]*num[i-K]

print(ans)
