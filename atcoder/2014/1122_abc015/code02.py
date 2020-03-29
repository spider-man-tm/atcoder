n = int(input())
a = list(map(int, input().split()))

from math import ceil, floor
#ceil()  # 切り上げ。常にup
#floor()  # 切り捨て。常にdown
#int()  # 常に0に近く（正負で挙動違う）

ans, cnt = 0, 0
for i in a:
    ans += i
    if i!=0:
        cnt += 1

print(ceil(ans/cnt))