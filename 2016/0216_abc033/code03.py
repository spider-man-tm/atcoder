s = input()

ans, tmp = [], []
for i in range(len(s)):
    if i%2==0:
        tmp.append(s[i])
        if i==len(s)-1:
            ans.append(tmp)
    else:
        if s[i]=='+':
            ans.append(tmp)
            tmp = []

cnt = 0
for _list in ans:
    if '0' not in _list:
        cnt += 1

print(cnt)