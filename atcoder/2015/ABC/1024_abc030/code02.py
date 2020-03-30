n, m = map(int, input().split())

n = 360*((n*60+m)/720%1)
m = 360*(m/60)
r = abs(n-m)

if r>180:
    print(360 - r)
else:
    print(r)