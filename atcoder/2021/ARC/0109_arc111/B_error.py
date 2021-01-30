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
    
    # xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
uf = UnionFind(400001)
numbers = set()
flag = 'tree'

for _ in range(N):
    a, b = map(int, input().split())
    if uf.same(a, b):
        flag = 'not tree'
    uf.union(a, b)
    numbers.add(a)
    numbers.add(b)

if flag == 'tree':
    print(len(numbers) - 1)
else:
    print(len(numbers))