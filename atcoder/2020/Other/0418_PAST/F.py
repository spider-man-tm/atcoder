from heapq import (
    heapify,  # 優先度付きキューの生成
    heappop,  # キューから値を取り出す
    heappush,   # キューに値を格納
    heappushpop,   # push -> popの順
    heapreplace,   # pop -> pushの順
)

N = int(input())
task = [[] for _ in range(N+1)]

heap = []
heapify(heap)
total = 0

for _ in range(N):
    A, B = map(int, input().split())
    task[A].append(-B)

for k in range(1, N+1):
    for t in task[k]:
        heappush(heap, t)

    total += -heappop(heap)
    print(total)
