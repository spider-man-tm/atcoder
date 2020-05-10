N = int(input())
S = [list(input()) for _ in range(N)]

for i in list(reversed(range(N-1))):
    tmp = S[i]
    tmp_low = S[i+1]
    for j in range(2*N-1):
        if tmp[j]=='#':
            if tmp_low[j-1]=='X' or tmp_low[j]=='X' or tmp_low[j+1]=='X':
                S[i][j] = 'X'

for row in S:
    print(''.join(row))