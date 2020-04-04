from heapq import (
    heapify,  # 優先度付きキューの生成
    heappop,
    heappush,
    heappushpop,
    heapreplace
    )

N, M = map(int, input().split())

#heapqは最小値しか取り出さないので-1倍する
A = [-i for i in map(int,input().split())]
heapify(A)

for _ in range(M):
    s = -heappop(A)
    s //= 2
    heappush(A, -s)

print(-sum(A))