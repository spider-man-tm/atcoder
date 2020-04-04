n = int(input())
total = 0

dic = {}

for i in range(1, 10):
    for j in range(1, 10):
        seki = i * j
        dic['{} x {}'.format(i, j)] = seki
        total += seki

dif = total-n
ans = []

for k, v in dic.items():
    if v == dif:
        ans.append(k)

ans = sorted(ans)

for i in ans:
    print(i)