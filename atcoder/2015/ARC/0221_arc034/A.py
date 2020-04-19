N = int(input())
ans = 0
for _ in range(N):
    a, b, c, d, e = map(int, input().split())
    score = a + b + c + d + (e*110/900)
    ans = max(ans, score)

print(ans)