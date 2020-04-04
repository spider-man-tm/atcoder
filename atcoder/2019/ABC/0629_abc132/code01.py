s = input()

dic = {}

for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for k, v in dic.items():
    if v != 2:
        print('No')
        exit()

print('Yes')