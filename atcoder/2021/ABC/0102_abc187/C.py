N = int(input())
ss = []
for _ in range(N):
    ss.append(input())
ss = set(ss)

ss = sorted(list(ss))

i = 0
for i in range(len(ss)):
    if ss[i][0] != '!':
        break

tmp = ss[:i]
tmp2 = ss[i:]

j_start = 0

for s in tmp:
    s = s[1:]
    for j in range(j_start, len(tmp2)):
        if tmp2[j] == s:
            print(s)
            exit()
        l1 = [s, tmp2[j]]
        l2 = sorted([s, tmp2[j]])
        if l1 == l2:
            j_start = j
            break

print('satisfiable')
