n = int(input())
l = sorted(list(map(int, input().split())))

last = l[-1]
total = sum(l[:-1])

if total>last:
    print('Yes')
else:
    print('No')