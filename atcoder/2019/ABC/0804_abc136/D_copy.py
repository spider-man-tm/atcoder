S = input()
N = len(S)
ans = []

def cal(R_count, L_count, ans):
    ans += [0] * (R_count-1)   # 中央の'RL'以外は全て0
    ans.append((R_count+1)//2 + (L_count//2))
    ans.append((L_count+1)//2 + (R_count//2))
    ans += [0] * (L_count-1)   # 中央の'RL'以外は全て0

R_count, L_count, i = 0, 0, 0
while i<N:
    if S[i]=='R':
        R_count += 1
        i += 1
    else:
        while i<N and S[i]=='L':
            L_count += 1
            i += 1
        cal(R_count, L_count, ans)
        R_count, L_count = 0, 0

print(*ans)