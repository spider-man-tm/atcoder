N, M = map(int, input().split())
switch = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
    cond = [0]*N
    for j in range(N):
        if 1&(i>>j):  # 右シフトして論理積（bit全探索）
            cond[j] = 1
    
    flag = True
    # print('cond: ', cond)
    for i in range(M):
        cnt = 0
        for j in switch[i][1:]:
            cnt +=  cond[j-1]
        if cnt%2 != P[i]:
            flag = False
            break
    # print('flag: ', flag)
    # print()
    ans += flag

print(ans)