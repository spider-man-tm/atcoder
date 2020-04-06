N = int(input())
x = [input() for _ in range(N)] + ['.........']
cnt = 0
flag = False
for j in range(9):
    for i in range(N+1):
        if flag:
            if x[i][j] != 'o':
                flag = False
                cnt += 1

                if x[i][j] == 'x':
                    cnt += 1
        else:
            if x[i][j]=='x':
                cnt += 1
            elif x[i][j]=='o':
                if flag==False:
                    flag = True

print(cnt)