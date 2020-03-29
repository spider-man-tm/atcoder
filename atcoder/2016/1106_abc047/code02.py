w, h, n = map(int, input().split())
xya = []

left = 0
right = w
under = 0
upper = h

for _ in range(n):
    x, y, a = map(int, input().split())

    if a==1:
        left = max(x, left)
    elif a==2:
        right = min(x, right)
    elif a==3:
        under = max(y, under)
    else:
        upper = min(y, upper)

if (upper-under)>0 and (right-left)>0:
    ans = (upper-under)*(right-left)
    print(ans)
else:
    print(0)