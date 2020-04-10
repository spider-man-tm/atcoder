A, B = map(int, input().split())
A = abs(0-A)
B = abs(0-B)

if A<B:
    print('Ant')
elif B<A:
    print('Bug')
else:
    print('Draw')