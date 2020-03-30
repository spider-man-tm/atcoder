a, b, c = map(int, input().split())
_list = sorted([a, b, c], reverse=True)
print(_list[0]*10 + _list[1] + _list[2])