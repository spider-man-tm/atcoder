X, Y = map(int, input().split())

for i in range(X+1):
    foot = i*2 + (X-i)*4
    if foot == Y:
        print('Yes')
        exit()

print('No')