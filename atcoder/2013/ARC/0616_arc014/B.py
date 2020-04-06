N = int(input())
W = [input() for _ in range(N)]
l = [W[0]]

for i in range(1, N):
    if W[i][0] != W[i-1][-1]:
        ans = 'WIN' if i%2==1 else 'LOSE'
        print(ans)
        exit()
    if W[i] in l:
        if i%2==0:
            print('LOSE')
            exit()
        if i%2==1:
            print('WIN')
            exit()
    else:
        l.append(W[i])

print('DRAW')