N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0

for i in range(N-1):
    now = X[i]
    nex = X[i+1]
    a = (nex - now) * A
    ans += min(a, B)

print(ans)