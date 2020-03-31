# よく使うモジュールや環境変数
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate
from itertools import product
from bisect import bisect_left,bisect_right
import heapq
from math import floor, ceil
from operator import itemgetter
inf = 10**17
mod = 10**9 + 7



# 辞書の最大値を取ってくる
max_kv_list = [kv for kv in d.items() if kv[1] == max(d.values())]
print(max_kv_list)
# [('a', 100), ('d', 100)]

max_k_list = [kv[0] for kv in d.items() if kv[1] == max(d.values())]
print(max_k_list)
# ['a', 'd']



# a ~ z までの辞書を生成(valueの初期値は0)
d = {chr(i): 50 for i in range(97, 97+26)}


# Union Find
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())