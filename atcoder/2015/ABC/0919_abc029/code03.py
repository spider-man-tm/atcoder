from itertools import product
n = int(input())

for v in list(product(['a', 'b', 'c'], repeat=n)):
    print(*v, sep='')