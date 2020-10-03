s = list(input())[::-1]

if len(s) == 1:
    print(*s)
    exit()

i = 0
while True:
    if s[i] == 'A' and s[i+1] == 'W':
        s[i] = 'C'
        s[i+1] = 'A'
    i += 1
    if i == len(s)-1:
        break

s = s[::-1]
print(*s, sep="")