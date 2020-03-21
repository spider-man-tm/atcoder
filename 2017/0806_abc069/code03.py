n = int(input())
a = list(map(int, input().split()))

n1, n2, n4 = 0, 0, 0
for i in a:
    if i%4==0:
        n4 += 1
    elif i%2==0:
        n2 += 1
    else:
        n1 += 1

if n2==0:
    if n1-1 <= n4:
        print('Yes')
    else:
        print('No')
else:
    if n1 <= n4:
        print('Yes')
    else:
        print('No')