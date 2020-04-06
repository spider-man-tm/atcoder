N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

diff = N-M

if diff==0:
    flag = True
    for i in range(M):
        for j in range(M):
            if B[i][j] != A[i][j]:
                flag = False
                break

        if flag==False:
            break
        
    if flag:
        print('Yes')
        exit()

else:
    for di in range(diff):
        for dj in range(diff):
            flag = True
            for i in range(M):
                for j in range(M):
                    if B[i][j] != A[i+di][j+dj]:
                        flag = False
                        break

                if flag==False:
                    break
                
            if flag:
                print('Yes')
                exit()

print('No')