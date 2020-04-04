N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(N-1):
    tmp = A[i+1] - A[i]

    if tmp==0:
        print('stay')
    elif tmp>0:
        print('up', tmp)
    else:
        print('down', abs(tmp))