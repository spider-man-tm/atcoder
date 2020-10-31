N = int(input())
x, y = map(int, input().split())

ans = 0

for _ in range(N-1):
    xx, yy = map(int, input().split())
    ans += abs(x - xx) + abs(y - yy)
    x, y = xx, yy

print(ans)