S = list(input())
T = list(input())

s, t = len(S), len(T)
ans = s

for i in range(s-t+1):
    tmp = S[i:i+t]

    cnt = 0
    for i, j in zip(T, tmp):
        if i != j:
            cnt += 1

    ans = min(ans, cnt)

print(ans)