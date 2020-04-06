sd = []
n, a, b = map(int, input().split())

for _ in range(n):
    s, d = input().split()
    sd.append([s, int(d)])

ans = 0
for s, d in sd:
    if d<a:
        d = a
    elif d>b:
        d = b
    
    if s == 'East':
        ans += d
    else:
        ans -= d

if ans<0:
    print('West', abs(ans))
elif ans>0:
    print('East', ans)
else:
    print(0)