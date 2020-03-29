n, T = map(int, input().split())
ct = []
for _ in range(n):
    c, t = map(int, input().split())
    ct.append([c, t])

ct = sorted(ct)
for c, t in ct:
    if t<=T:
        print(c)
        exit()

print('TLE')