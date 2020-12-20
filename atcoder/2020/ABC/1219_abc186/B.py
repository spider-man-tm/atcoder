H, W = map(int, input().split())
mini = float('inf')

hai = []

for _ in range(H):
    A = list(map(int, input().split()))
    mi = min(A)
    mini = min(mini, mi)
    hai.append(A)

ans = 0
for i in range(H):
    li = hai[i]
    for i in li:
        ans += (i - mini)

print(ans)