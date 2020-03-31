S = input()
dic = {'a': 0, 'b':0, 'c':0}

for c in S:
    dic[c] += 1

l = [dic['a'], dic['b'], dic['c']]
if max(l)-min(l) <= 1:
    print('YES')
else:
    print('NO')