H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

ans = 0
for i in range(H):
    tmp = S[i]
    for i in range(W-1):
        if tmp[i] == '.' and tmp[i+1] == '.':
            ans += 1

for j in range(W):
    tmp = ''
    for i in range(H):
        tmp += S[i][j]
    for i in range(H-1):
        if tmp[i] == '.' and tmp[i+1] == '.':
            ans += 1

print(ans)