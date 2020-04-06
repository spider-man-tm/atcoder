from datetime import *

N = int(input())
holiday = []
for i in range(N):
    m, d = map(int, input().split('/'))
    t = (date(2012, m, d) - date(2012, 1, 1)).days
    holiday.append(t)

ans = 0
cnt = 0
hurikae = 0

for i in range(366):
    if i%7==0 or i%7==6:
        cnt += 1
        if i in holiday:
            hurikae += 1
    elif i in holiday:
        cnt += 1
    else:
        if hurikae > 0:
            hurikae -= 1
            cnt += 1
        else:
            cnt = 0
    
    ans = max(ans, cnt)

print(ans)