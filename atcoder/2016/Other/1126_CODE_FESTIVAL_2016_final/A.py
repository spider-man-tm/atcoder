H, W = map(int, input().split())
S = [list(input().split()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == 'snuke':
            i += 1
            j += 65
            print(chr(j), i, sep='')
            break