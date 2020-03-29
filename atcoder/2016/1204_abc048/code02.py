a, b, x = map(int, input().split())

if a%x==0:
    ax = a//x-1
else:
    ax = a//x

bx = b//x

print(bx-ax)