n = int(input())
a = list(map(int, input().split()))
_list = [[h, i] for i, h in enumerate(a)]
_list = sorted(_list, reverse=True)

for _, i in _list:
    print(i+1)