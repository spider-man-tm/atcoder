n, m, x = map(int, input().split())
a = list(map(int, input().split()))

right = 0
for r in range(x, n+1):
    if r in a:
        right += 1

left = 0
for l in range(x):
    if l in a:
        left += 1

print(min(right, left))