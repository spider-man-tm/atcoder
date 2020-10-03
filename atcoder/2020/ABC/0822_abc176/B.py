N = input()

cnt = 0
for i in range(len(N)):
    cnt += int(N[i])

if cnt % 9 == 0:
    print('Yes')
else:
    print('No')