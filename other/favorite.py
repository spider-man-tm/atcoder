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


# 深いネストをスマートに書く
import itertools as itr
a = ['a','b','c']
b = ['5','6','7']
c = ['d','e','f']
d = ['1','2','3']

for w,x,y,z in itr.product(a,b,c,d):
    print(w,x,y,z)



# 最大公約数（ユークリッドの互除法）
import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)



# 複数のリストを同時にソートする
_list = [[3, 'agr', 'あ'], [0, 'bde', 'い'], [3, 'rfb', 'う']]
_list = sorted(_list, key=lambda x: (-x[0], x[2]))
print(_list)
"""
[[3, 'agr', 'あ'], [3, 'rfb', 'う'], [0, 'bde', 'い']]
#一優先キーが先頭の数字(降順)。第二優先キーが平仮名
"""



# listの要素を数える
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)
print(c)   # Counter({'a': 4, 'c': 2, 'b': 1})



# 辞書の最大値を取ってくる
max_kv_list = [kv for kv in d.items() if kv[1] == max(d.values())]
print(max_kv_list)
# [('a', 100), ('d', 100)]

max_k_list = [kv[0] for kv in d.items() if kv[1] == max(d.values())]
print(max_k_list)
# ['a', 'd']



# a ~ z までの辞書を生成(valueの初期値は0)
d = {chr(i): 50 for i in range(97, 97+26)}



# 組み合わせとか順列の列挙
# https://note.nkmk.me/python-math-factorial-permutations-combinations/
# (以下、よく使う例)
l = ['a', 'b', 'c', 'd']
c = itertools.combinations(l, 2)
print(type(c))
# <class 'itertools.combinations'>
for v in itertools.combinations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'c')
# ('b', 'd')
# ('c', 'd')

# 組み合わせの総数を出す
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
print(combinations_count(4, 2))
# 6