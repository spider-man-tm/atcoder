n, x = map(int, input().split())
l = list(map(int, input().split()))

point, cnt = 0, 1
for i in range(n):
    point += l[i]
    if point>x:
        break
    cnt += 1

print(cnt)