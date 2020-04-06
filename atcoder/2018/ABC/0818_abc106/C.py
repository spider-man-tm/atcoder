s = input()
k = int(input())
flag = False

for i in range(min(len(s), k)):
    if s[i] != '1':
        ans = int(s[i])
        flag = True
        break

if flag:
    print(ans)
else:
    print(1)