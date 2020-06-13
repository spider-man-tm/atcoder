N, A, B = map(int, input().split())

mod = N % (A + B)

if mod > A or mod == 0:
    print('Bug')
else:
    print('Ant')