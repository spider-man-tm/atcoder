n, k = map(int, input().split())
h = sorted([int(input()) for _ in range(n)])


ans = 10**9
for i in range(n-k+1):
    diff = h[i+k-1] - h[i]
    if diff < ans:
        ans = diff

print(ans)