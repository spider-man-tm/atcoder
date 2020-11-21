A, B, C = map(int, input().split())
l = sorted([A, B, C])

if l[1] == A:
    print('A')
elif l[1] == B:
    print('B')
else:
    print('C')