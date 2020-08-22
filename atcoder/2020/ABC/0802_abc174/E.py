from heapq import (
    heapify,  # 優先度付きキューの生成
    heappop,  # キューから値を取り出す
    heappush,   # キューに値を格納
    heappushpop,   # push -> popの順
    heapreplace,   # pop -> pushの順
    )
from math import ceil, floor
#ceil()  # 切り上げ。常にup
#floor()  # 切り捨て。常にdown
#int()  # 常に0に近く（正負で挙動違う）
#round(f),  round(f, 1)  # 四捨五入（第二引数で小数点桁数を指定）

N, K = map(int, input().split())
A = [-i for i in map(int,input().split())]
heapify(A)

for i in range(K):
    s = -heappop(A)
    if (K - i) > len(A):
        t = s / 3
        heappush(A, -(s - t))
        heappush(A, -t)
    else:
        s = s / 2
        heappush(A, -s)
        heappush(A, -s)

    print(A)      

print(ceil(-heappop(A)))
