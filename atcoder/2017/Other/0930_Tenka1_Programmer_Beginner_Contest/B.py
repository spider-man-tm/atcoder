N = int(input())

amin, amax, bmin = float('inf'), 0, float('inf')

for _ in range(N):
    A, B = map(int, input().split())
    amin = min(amin, A)
    amax = max(amax, A)
    bmin = min(bmin, B)

ans = (amin-1) + (amax-amin+1) + bmin
print(ans)