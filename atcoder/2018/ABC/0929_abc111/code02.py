n = int(input())

for i in range(n, 1000):
    s = str(i)
    if s[0]==s[1]==s[2]:
        break

print(int(s))