H, W = map(int, input().split())
S = ['.' + input() + '.' for _ in range(H)]
S = ['.'*(W+2)] + S + ['.'*(W+2)]
ans = [[0]*W for _ in range(H)]

for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i][j] != '#':
            tmp = S[i-1][j-1]=='#'
            tmp += S[i][j-1]=='#'
            tmp += S[i+1][j-1]=='#'
            tmp += S[i+1][j]=='#'
            tmp += S[i+1][j+1]=='#'
            tmp += S[i][j+1]=='#'
            tmp += S[i-1][j+1]=='#'
            tmp += S[i-1][j]=='#'
            tmp = str(tmp)
        else:
            tmp = '#'
        ans[i-1][j-1] = tmp
        
for i in ans:
    print(*i, sep='')