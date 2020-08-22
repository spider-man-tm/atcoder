W = set(input())
L = list(input().split())

cnt = 0
total = set()

for l in L:
    if l not in total:
        total.add(l)
        cnt += W == set(l)

print(cnt)
