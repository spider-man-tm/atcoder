N = int(input())
R = []
for _ in range(N):
    X, L = map(int, input().split())
    l, r = X-L, X+L
    R.append([l, r])

R = sorted(R, key=lambda x: x[1])
tmp = R[0]
ans = [R[0]]
for i in range(1, N):
    v = R[i]
    if tmp[1] <= v[0]:
        ans.append(v)
        tmp = v

print(len(ans))