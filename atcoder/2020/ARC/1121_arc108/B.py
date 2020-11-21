N = int(input())
s = list(input())

t = []

for i in range(N):
    t.append(s[i])

    if len(t) >= 3:
        if t[-3] == 'f' and t[-2] == 'o' and t[-1] == 'x':
            del t[-3:]

print(len(t))