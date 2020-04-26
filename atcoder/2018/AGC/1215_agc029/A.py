S = input()
total_w = [0]*len(S)
cnt_w = S.count('W')

cnt = 0
for i in range(len(S)):
    if S[i]=='W':
        cnt += 1
    total_w[i] = cnt_w - cnt

ans = 0
for i in range(len(S)):
    if S[i]=='B':
        ans += total_w[i]

print(ans)