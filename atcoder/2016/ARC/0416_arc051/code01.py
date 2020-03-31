x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

if x2 <= (x1-r) and (x1+r) <= x3:
    if y2 <= (y1-r) and (y1+r) <= y3:
        ans1 = 'NO'
    else:
        ans1 = 'YES'
else:
    ans1 = 'YES'

d1 = (x2-x1)**2 + (y2-y1)**2
d2 = (x3-x1)**2 + (y2-y1)**2
d3 = (x2-x1)**2 + (y3-y1)**2
d4 = (x3-x1)**2 + (y3-y1)**2

if d1<=r**2 and d2<=r**2 and d3<=r**3 and d4<=r**4:
    ans2 = 'NO'
else:
    ans2 = 'YES'

print(ans1)
print(ans2)