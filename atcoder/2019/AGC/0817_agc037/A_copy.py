S = input()
pre = '#'
cur = ''
cnt = 0

for i in range(len(S)):
    cur += S[i]
    if pre != cur:
        cnt += 1
        pre = cur
        cur = ''

print(cnt)