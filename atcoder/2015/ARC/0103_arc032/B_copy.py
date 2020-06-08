class UnionFind:
    def __init__(self, n):
        self.par = list(range(n)) #親
        self.rank = [0] * n #根の深さ

    # xの属する根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じ集合に属するかを判定（同じ根に属するか）
    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
uf = UnionFind(N)

#print(uf.par)   # [0, 1, 2, 3, 4, 5] 併合前で親なし
#print(uf.rank)   # [0, 0, 0, 0, 0, 0] 木の深さは全て0

for _ in range(M):
    a, b = map(int, input().split())
    uf.unite(a-1, b-1)

#print(uf.par)   # [0, 0, 0, 3, 4, 4]
#print(uf.rank)   # [1, 0, 0, 0, 1, 0]

ans = -1
 
for i in range(N):
  if uf.par[i] == i:
    ans += 1

print(ans)