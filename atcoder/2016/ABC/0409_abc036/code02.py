n = int(input())
s = [input() for _ in range(n)]

for j in range(n):
    for i in range(n):
        i = n-1-i
        print(s[i][j], sep='', end='')
    print()