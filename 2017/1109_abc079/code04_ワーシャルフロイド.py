h, w = map(int, input().split())
c = []
a = []

for _ in range(10):
    c.append(list(map(int, input().split())))

for _ in range(h):
    a.append(list(map(int, input().split())))

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1:
            ans += c[a[i][j]][1]  # 1までの最短コスト

print(ans)