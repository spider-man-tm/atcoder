s = input()
before = s[0]
cnt = 1
ans = []
for i in range(1, len(s)):
    if i != len(s)-1:
        if s[i]==before:
            cnt += 1
        else:
            ans.append(before)
            ans.append(cnt)
            cnt = 1
            before = s[i]
    else:
        if s[i]==before:
            cnt += 1
            ans.append(before)
            ans.append(cnt)
        else:
            ans.append(before)
            ans.append(cnt)
            ans.append(s[i])
            ans.append(1)


for a in ans:
    print(a, end='')
print()