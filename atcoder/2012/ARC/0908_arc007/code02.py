N, M = map(int, input().split())

cd = list(range(1, N+1))
now = 0

for _ in range(M):
    d = int(input())
    if d != now:
        ix = cd.index(d)
        now, cd[ix] = d, now

for i in cd:
    print(i)