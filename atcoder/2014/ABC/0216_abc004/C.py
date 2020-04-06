n = int(input())
_list = [1, 2, 3, 4, 5, 6]

n = n%30
if n==0:
    for i in _list:
        print(i, end='')
    print()
    exit()

for i in range(n):
    _list[i%5], _list[i%5+1] = _list[i%5+1], _list[i%5]

for i in _list:
    print(i, end='')
print()