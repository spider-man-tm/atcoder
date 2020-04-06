a, b, c, x, y = map(int, input().split())

p1 = 2*c * max(x, y)
p2 = a*x + b*y
p3 = 2*c * min(x, y) + a*(x-min(x, y)) + b*(y-min(x, y))

print(min(p1, p2, p3))