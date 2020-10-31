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


N, M = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

union = UnionFind(N)

for _ in range(M):
    c, d = map(int, input().split())
    union.union(c-1, d-1)

group = []
for i in range(N):
    group.append(union.find(i))

cnt_a, cnt_b = {}, {}
for i in range(N):
    g = group[i]
    if g in cnt_a:
        cnt_a[g] += a[i]
        cnt_b[g] += b[i]
    else:
        cnt_a[g] = a[i]
        cnt_b[g] = b[i]

for k, v in cnt_a.items():
    if cnt_b[k] != v:
        print('No')
        exit()

print('Yes')