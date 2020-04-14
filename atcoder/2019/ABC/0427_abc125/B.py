n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

vc = []
for i in range(n):
    vc.append(v[i]-c[i])

vc = sorted(vc, reverse=True)
ans = 0
for i in range(n):
    if vc[i]>0:
        ans += vc[i]

print(ans)