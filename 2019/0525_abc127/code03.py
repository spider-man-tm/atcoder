n, m = map(int, input().split())
mini, maxi = 0, 10**5+1

for _ in range(m):
    l, r = map(int, input().split())
    if l>mini:
        mini = l
    if r<maxi:
        maxi = r

print(max((maxi-mini+1), 0))