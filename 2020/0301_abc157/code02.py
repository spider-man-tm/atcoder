A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A = [A1, A2, A3]
n = int(input())
b = []
for _ in range(n):
    b.append(int(input()))

AA = [[False, False, False],
[False, False, False],
[False, False, False]]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            AA[i][j] = True

if AA[0][0] and AA[0][1] and AA[0][2]:
    print('Yes')
elif AA[1][0] and AA[1][1] and AA[1][2]:
    print('Yes')
elif AA[2][0] and AA[2][1] and AA[2][2]:
    print('Yes')
elif AA[0][0] and AA[1][0] and AA[2][0]:
    print('Yes')
elif AA[0][1] and AA[1][1] and AA[2][1]:
    print('Yes')
elif AA[0][2] and AA[1][2] and AA[2][2]:
    print('Yes')
elif AA[0][0] and AA[1][1] and AA[2][2]:
    print('Yes')
elif AA[0][2] and AA[1][1] and AA[2][0]:
    print('Yes')
else:
    print('No')