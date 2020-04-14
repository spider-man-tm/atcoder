N, L = map(int, input().split())
S = list(input())

tab = 1
cnt = 0
for i in range(N):
    if S[i]=='+':
        tab += 1
    else:
        tab -= 1
    
    if tab == L+1:
        tab = 1
        cnt += 1

print(cnt)