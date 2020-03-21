n, m, x, y = map(int, input().split())
x = list(map(int, input().split())) + [x]
y = list(map(int, input().split())) + [y]

if max(x)<min(y):
    print('No War')
else:
    print('War')