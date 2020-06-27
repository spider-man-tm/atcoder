s = input().split()

N = int(input())

for _ in range(N):
    t = input()
    for i in range(len(s)):
        if '*' not in list(t):
            if s[i] == t:
                s[i] = '*'*len(s[i])
        else:
            if len(s[i])==len(t):
                flag = True
                for j in range(len(s[i])):
                    if s[i][j] != t[j]:
                        if s[i][j] != '*' and t[j] != '*':
                            flag = False
                            break
                if flag:
                    s[i] = '*'*len(s[i])

print(*s)