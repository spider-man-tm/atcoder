N = int(input())

ans = 0

for _ in range(N):
    A, B = map(int, input().split())
    ans += min(A//2, B)

print(ans)