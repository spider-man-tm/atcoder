x = int(input())
ans = 0
for b in range(1, 100):
    for p in range(2, 100):
        bp = b**p
        if bp<=x:
            ans = max(ans, bp)
print(ans)