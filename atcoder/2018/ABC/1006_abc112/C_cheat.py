from itertools import product

N = int(input())
point = []
H = 0
flag = False

for _ in range(N):
    x, y, h = map(int, input().split())
    point.append((x, y, h))
point = sorted(point, key=lambda x: x[2], reverse=True)

for v in product(range(101), range(101)):
    Cx, Cy = v[0], v[1]
    flag = True
    for i, (x, y, h) in enumerate(point):
        if i == 0:
            H = abs(x - Cx) + abs(y - Cy) + h
        else:
            HH = max(H - abs(x - Cx) - abs(y - Cy), 0)
            if HH != h:
                flag = False
                break

    if flag:
        print(Cx, Cy, H)
        exit()
