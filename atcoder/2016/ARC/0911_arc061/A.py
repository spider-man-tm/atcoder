S = list(input())
N = len(S)-1

def cal(l):
    c = ''
    for i in range(len(l)):
        if i%2==0:
            c += l[i]
        else:
            if l[i]==1:
                c += '+'
    return eval(c)

ans = 0
for i in range(1<<N):
    cond = [0]*N
    for j in range(N):
        if 1&(i>>j):  # 右シフトして論理積（bit全探索）
            cond[j] = 1
    tmp = []
    for i in range(N):
        tmp.append(S[i])
        tmp.append(cond[i])
    tmp.append(S[-1])

    ans += cal(tmp)

print(ans)