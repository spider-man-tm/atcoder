n = int(input())
flag = False

for i in range(1, 10):
    for j in range(1, 10):
        if i*j==n:
            flag=True
            break
    if flag:
        break

if flag:
    print('Yes')
else:
    print('No')
            