N = int(input())

ans = 0

for _ in range(N):
    A, B = map(int, input().split())
    ans = max(ans, A + B)

print(ans)