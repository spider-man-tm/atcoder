n = int(input())
s, p = [], []
for _ in range(n):
    i, j = input().split()
    s.append(i);  p.append(int(j))

total = sum(p)
half = total/2
ans = 'atcoder'

for i, j in zip(s, p):
    if j>half:
        ans = i
        break

print(ans)