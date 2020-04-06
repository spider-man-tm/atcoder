n = int(input())
ss = input()

ans = 1
s_before = ss[0]
for s in ss:
    if s != s_before:
        ans += 1
        s_before = s

print(ans)