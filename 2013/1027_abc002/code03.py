xa, ya, xb, yb, xc, yc = map(int, input().split())

x1 = xa-xa
x2 = xb-xa
x3 = xc-xa
y1 = ya-ya
y2 = yb-ya
y3 = yc-ya

s = abs(x2*y3 - y2*x3)/2
print(s)