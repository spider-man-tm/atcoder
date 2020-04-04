n = int(input())
a = list(map(int, input().split()))

x1 = sum(a) - 2*(sum(a[1::2]))

for i in range(n):
    if i==0:
        x = x1
        before = x
    else:
        x = 2*a[i-1] - before
        before = x

    print(x, end=' ')

print()