A, R, N = map(int, input().split())

if R==1:
    print(A)

else:
    over = 10**9
    for i in range(N):
        if i>0:
            A *= R
            if A>over:
                print('large')
                exit()
    print(A)