S = input()
N = len(S)
if N != 26:
    for i in range(26):
        c = chr(97 + i)
        if not c in S:
            print(S + c)
            exit()
li = []
for i in reversed(range(26)):
    li.append(S[i])
    if i == 0:
        print(-1)
        exit()
    if S[i-1] < S[i]:
        e = i - 1
        break
li.sort()
for x in li:
    if S[e] < x:
        print(S[:e] + x)
        exit()
