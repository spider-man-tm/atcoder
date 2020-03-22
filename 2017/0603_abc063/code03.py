n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

s = sorted(s)
for i in range(n):
    i -= 1
    if i == -1:
        total = sum(s)
    else:
        total = sum(s) - s[i]

    if total%10 != 0:
        print(total)
        exit()

print(0)