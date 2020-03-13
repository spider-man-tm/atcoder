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


# 組み合わせとか順列の列挙
