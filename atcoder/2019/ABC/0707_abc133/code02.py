import itertools as ite


def dist_cal(point_i, point_j):
    total = 0
    for i, j in zip(point_i, point_j):
        total += (i-j)**2
    return total ** (1/2)


n, d = map(int, input().split())

x = []
for i in range(n):
    _list = list(map(int, input().split()))
    x.append(_list)

cmb = list(ite.combinations(x, 2))

cnt = 0
for i, j in cmb:
    dist = dist_cal(i, j)

    if dist == int(dist):
        cnt += 1

print(cnt)