n = int(input())
res = []
sco = []
idx = []

for i in range(n):
    _list = list(input().split())
    _list.append(i+1)
    res.append(_list)

res = sorted(res, key=lambda x: (x[0], -int(x[1])))

for i, j, k in res:
    print(k)