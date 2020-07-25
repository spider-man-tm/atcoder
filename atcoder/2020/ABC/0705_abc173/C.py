H, W, K = map(int, input().split())
C = []

for _ in range(H):
    C.append(input())


def check(C, row, col):
    cnt = 0
    for i in range(H):
        for j in range(W):
            if row[i] == 0 and col[j] == 0 and C[i][j] == '#':
                cnt += 1

    return cnt
            
ans = 0
for i in range(1<<H):
    row = [0]*H
    for j in range(H):
        if 1&(i>>j):  # 右シフトして論理積（bit全探索）
            row[j] = 1

    for i in range(1<<W):
        col = [0]*W
        for j in range(W):
            if 1&(i>>j):  # 右シフトして論理積（bit全探索）
                col[j] = 1

        # print(row, col)
        if check(C, row, col) == K:
            ans += 1

print(ans)