A = [[0]+list(map(int, input().split()))+[0] for _ in range(4)]
A = [[0]*6] + A + [[0]*6]

for i in range(1, 5):
    for j in range(1, 5):
        tmp = A[i][j]
        if tmp == A[i-1][j]:
            print('CONTINUE')
            exit()
        elif tmp == A[i][j+1]:
            print('CONTINUE')
            exit()
        elif tmp == A[i+1][j]:
            print('CONTINUE')
            exit()
        elif tmp == A[i][j-1]:
            print('CONTINUE')
            exit()

print('GAMEOVER')