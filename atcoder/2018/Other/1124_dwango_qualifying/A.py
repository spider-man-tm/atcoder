N = int(input())
A = list(map(int, input().split()))
m = sum(A)/N
dif = [0]*N

for i in range(N):
    dif[i] = abs(m - A[i])

for i in range(N):
    if dif[i] == min(dif):
        print(i)
        exit()