n, s, t = map(int, input().split())
a = [int(input()) for i in range(n)]
w = 0
cnt = 0
for j in a:
    w += j
    if w >= s and w <= t:
        cnt += 1
print(cnt)