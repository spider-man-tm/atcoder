class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    # xの属する木の根を求める
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # xとyの属する集合のマージ
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    # xの属する集合の大きさを返す
    def size(self, x):
        return -self.parents[self.find(x)]
    
    # xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    # xと同じグループを返す
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    # 根ノードを返す
    # 複数存在する時はその分だけ返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    # グループ数を返す
    def group_count(self):
        return len(self.roots())
    
    # groupとそれに属するメンバーの辞書を返す
    # exp. {0: [0, 1, 4], 2: [2, 3]}
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    # 上記メソッド参照
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N, Q = map(int, input().split())
union = UnionFind(N+1)

for _ in range(Q):
    t, u, v = map(int, input().split())
    if t:
        if union.same(u, v):
            print(1)
        else:
            print(0)
    else:
        union.union(u, v)
