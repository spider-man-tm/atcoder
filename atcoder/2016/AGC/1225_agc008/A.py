x, y = map(int, input().split())

if 0 <= x <= y or x <= y <= 0:
    print(y - x)
elif x <= 0 <= y:
    if x == 0 or y == 0:
        print(abs(x + y))
    else:
        print(abs(y + x) + 1)
elif 0 <= y <= x or y <= x <= 0:
    if x == 0 or y == 0:
        print(abs(x - y) + 1)
    else:
        print(abs(x - y) + 2)
else:
    print(abs(x + y) + 1)