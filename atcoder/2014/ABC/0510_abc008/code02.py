n = int(input())
dic = {}

for _ in range(n):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

maxi = 0
ans = ''

for k, v in dic.items():
    if v>maxi:
        maxi = v
        ans = k

print(ans)