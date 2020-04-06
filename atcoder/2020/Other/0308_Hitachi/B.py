_, _, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(a) + min(b)

for _ in range(m):
    x, y, c = map(int, input().split())
    kaikei = a[x-1] + b[y-1] - c
    if kaikei < ans:
        ans = kaikei

print(ans)