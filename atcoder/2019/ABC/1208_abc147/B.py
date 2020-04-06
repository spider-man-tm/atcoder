s = input()

ans = 0
leng = len(s)
half = leng // 2
for i in range(half):
    if s[i] != s[leng-1-i]:
        ans += 1

print(ans)