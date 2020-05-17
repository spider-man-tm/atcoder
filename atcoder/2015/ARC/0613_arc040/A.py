N = int(input())
R, B = 0, 0

for i in range(N):
    s = input()
    R += s.count('R')
    B += s.count('B')

if R>B:
    print('TAKAHASHI')
elif B>R:
    print('AOKI')
else:
    print('DRAW')