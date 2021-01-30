N = int(input())
S = []

ans = 1
for _ in range(N):
    S.append(input())

for i in range(N)[::-1]:
    tmp = S[i]

    if tmp == 'OR':
        # 端がtrueであればOK
        ans += 2**(i+1)

print(ans)