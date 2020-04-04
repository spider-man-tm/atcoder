import heapq

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, 0])

    while len(q) > 0:
        # ヒープから取り出し
        print('q: ', q)
        print('dist: ', dist)
        _, u = heapq.heappop(q)
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新してヒープに登録
                dist[i[0]] = dist[u] + i[1]
                heapq.heappush(q, [dist[u] + i[1], i[0]])

    return dist

# 辺のリスト（終点とコストのリスト）
edges = [
    [[1, 4], [2, 3]],
    [[2, 1], [3, 1], [4, 5]],
    [[5, 2]],
    [[4, 3]],
    [[6, 2]],
    [[4, 1], [6, 4]],
    []
]
print(dijkstra(edges, 7))

"""
q:  [[0, 0]]
dist:  [0, inf, inf, inf, inf, inf, inf]
q:  [[3, 2], [4, 1]]
dist:  [0, 4, 3, inf, inf, inf, inf]
q:  [[4, 1], [5, 5]]
dist:  [0, 4, 3, inf, inf, 5, inf]
q:  [[5, 3], [5, 5], [9, 4]]
dist:  [0, 4, 3, 5, 9, 5, inf]
q:  [[5, 5], [9, 4], [8, 4]]
dist:  [0, 4, 3, 5, 8, 5, inf]
q:  [[6, 4], [9, 4], [8, 4], [9, 6]]
dist:  [0, 4, 3, 5, 6, 5, 9]
q:  [[8, 4], [8, 6], [9, 6], [9, 4]]
dist:  [0, 4, 3, 5, 6, 5, 8]
q:  [[8, 6], [9, 4], [9, 6]]
dist:  [0, 4, 3, 5, 6, 5, 8]
q:  [[9, 4], [9, 6]]
dist:  [0, 4, 3, 5, 6, 5, 8]
q:  [[9, 6]]
dist:  [0, 4, 3, 5, 6, 5, 8]
[0, 4, 3, 5, 6, 5, 8]
"""
