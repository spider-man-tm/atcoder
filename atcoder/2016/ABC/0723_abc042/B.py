n, l = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())

s = sorted(s)

for i in s:
    print(i, end='')
print()