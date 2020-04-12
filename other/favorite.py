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


##### 二分木 #####
class Node:
    def __init__(self, data): #コンストラクタ
        self.data = data #ノードがもつ数値
        self.left = None #左エッジ
        self.right = None #右エッジ


class BST:
    def __init__(self, number_list): #コンストラクタ
        self.root = None #ルートノード初期化
        for node in number_list: #数値を持つ配列から二分木を生成
            self.insert(node) #挿入メソッドを使ってノードを挿入する
    #挿入
    def insert(self, data):
        n = self.root
        if n == None:
            self.root = Node(data)
            return
        else:
            while True:
                entry = n.data
                if data < entry:
                    if n.left is None:
                        n.left = Node(data)
                        return
                    n = n.left
                elif data > entry:
                    if n.right is None:
                        n.right = Node(data)
                        return
                    n = n.right
                else:
                    n.data = data
                    return
    #検索機能(インターフェース)
    def search(self, search):
        searcher = self._search_bool(search)
        if searcher is None:
            print("Search target is not found.")
        elif searcher == True:
            print(str(search) + " is found!")
        elif searcher == False:
            print(str(search) + " is not found.")

    #検索機能本体(出力:boolean),深さ優先探索
    #nodeのvisitedはpopで代用
    def _search_bool(self, search):
        n = self.root
        if n is None:
            return None
        else:
            lst = []
            lst.append(n)
            while len(lst) > 0:
                node = lst.pop()
                if node.data == search:
                    return True
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)
            return False

    def inorder(self, node): #中順探索 l->r->p^n
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)


#整数列Aの生成---------------------------------------------
#ランダム整数列Aの生成
import random
iarray_A = list(range(50))
random.shuffle(iarray_A)
print(iarray_A)
#---------------------------------------------------------


#テスト----------------------------------------------------
tree = BST(iarray_A) #配列から二分探索木生成し、treeに代入
print('tree: ', tree.data)
#tree.search(10)#１０がtreeに存在するか検索
#tree.inorder(tree.root) #中順走査、１～順にソート
#---------------------------------------------------------