def diff(x, y):
    return x**2 + y**2

N, D = map(int, input().split())
D = D**2
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())
    d = x**2 + y**2
    if d <= D:
        cnt += 1

print(cnt)