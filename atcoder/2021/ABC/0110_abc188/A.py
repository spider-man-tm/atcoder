X, Y = map(int, input().split())

mini = min(X, Y)
maxi = max(X, Y)

if mini + 3 > maxi:
    print('Yes')
else:
    print('No')