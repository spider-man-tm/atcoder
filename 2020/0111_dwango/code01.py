n = int(input())

dic = {}
for i in range(n):
    dic[i] = input().split()

x = input()

start = 0

for i, (k, v) in enumerate(dic.items()):
    if v[0] not in [x]:
        pass
    else:
        start = i+1
        break

if start==0:
    print(0)

else:
    ans = 0
    for i, (k, v) in enumerate(dic.items()):
        if i < start:
            pass
        else:
            ans += int(v[1])
    print(ans)