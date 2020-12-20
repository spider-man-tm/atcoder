r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = abs(r1 - r2)
c = abs(c1 - c2)

if r1 == r2 and c1 == c2:
    print(0)

# 1手で行ける
elif r == c:
    print(1)
elif r <= 2 and c <= 2:
    print(1)
elif r == 3 and c2 == c1:
    print(1)
elif c == 3 and r2 == r1:
    print(1)

# 2手で行ける
elif r % 2 == 0 and c % 2 == 0:
    print(2)
elif r % 2 == 1 and c % 2 == 1:
    print(2)
elif abs(r - c) <= 3:
    print(2)
elif r + c <= 6:
    print(2)
    
else:
    print(3)