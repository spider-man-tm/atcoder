n = int(input())
s = {}
ans = 0
for _ in range(n):
    sn = sorted(input())
    sn = ''.join(sn)

    if sn in s:
        ans += s[sn]
        s[sn] += 1
    else:
        s[sn] = 1

print(ans)