n = int(input())
s = []
for _ in range(n):
    si = input()
    si = list(reversed([c for c in si]))
    s.append(si)

s = sorted(s)
for i in s:
    i = list(reversed(i))
    print(''.join(i))