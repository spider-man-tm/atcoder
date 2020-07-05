S = list(input())

ans = 0
for i in range(len(S)):
    up = len(S) - (i + 1)
    do = i

    if S[i] == 'U':
        ans += up + do * 2
    else:
        ans += up * 2 + do

print(ans)