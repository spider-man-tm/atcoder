N, M, A, B = map(int, input().split())
c = [int(input()) for _ in range(M)]

for i in range(M):
    if N<=A:
        N += B
    N -= c[i]

    if N<0:
        print(i+1)
        exit()

print('complete')