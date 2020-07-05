from collections import Counter
#l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
#c = Counter(l)
#print(c)   # Counter({'a': 4, 'c': 2, 'b': 1})

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    # xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # xとyの属する集合のマージ
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

    # xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M, K = map(int, input().split())
tree = UnionFind(N)
friend = [[] for _ in range(N)]
block = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    tree.unite(A-1, B-1)
    friend[A-1].append(B-1)
    friend[B-1].append(A-1)

for _ in range(K):
    C, D = map(int, input().split())
    block[C-1].append(D-1)
    block[D-1].append(C-1)

group_count = Counter(tree.par)

print()
print(tree.par)
print(group_count)
print()

ans = []
for i in range(N):
    cnt = 0
    g = tree.par[i]
    cnt += group_count[g]
    print(cnt)
    #cnt -= len(friend[i]) + len(block[i]) + 1
    ans.append(cnt)
    #print(cnt)
    print()

print(*ans)