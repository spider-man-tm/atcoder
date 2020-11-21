N = int(input())
ans = 0

for _ in range(N):
    a, b = map(int, input().split())
    ans += int((a+b) * (b-a+1)/2)

print(ans)