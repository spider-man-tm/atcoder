N = int(input())
A = [0]*N
relation = []
for i in range(N):
    tmp = []
    A[i] = int(input())
    for j in range(A[i]):
        tmp.append(list(map(int, input().split())))
    relation.append(tmp)

ans = 0
for i in range(1<<N):
    cond = [0]*N
    for j in range(N):
        if 1&(i>>j):  # 右シフトして論理積（bit全探索）
            cond[j] = 1

    mujun = False
    stop_flag = False
    for j in range(N):  # 一人一人判定

        # 正直者の時だけ判定
        # 不親切の場合、特に判定はしない（嘘でも本当でも良いので）
        if cond[j] == 1:
            for k in range(A[j]):  # jの証言を一つずつチェック
                #print(cond[rel[j][k][0]-1])
                #print(rel[j][k][1])
                if cond[relation[j][k][0]-1] != relation[j][k][1]:  # jのk番目の証言をチェック
                    mujun = True
                    stop_flag = True
                    break

        if stop_flag:
            break
    
    if not mujun:
        ans = max(ans, sum(cond))

print(ans)