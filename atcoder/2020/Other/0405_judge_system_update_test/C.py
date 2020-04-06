from itertools import permutations
a, b, c = map(int, input().split())
A = [[100]*4 for i in range(4)]
l = [i for i in range(1, a+b+c+1)]
ans = 0

for v in permutations(l, a+b+c):
    for i in range(a):
        A[0][i] = v[i]
    for i in range(a, a+b):
        A[1][i-a] = v[i]
    for i in range(a+b, a+b+c):
        A[2][i-a-b] = v[i]

    flag = False
    for i in range(3):
        if flag:
            break
        for j in range(3):
            if A[i][j] > A[i][j+1] or A[i][j] > A[i+1][j]:
                flag = True
                break

    if flag==False:
        ans += 1

print(ans)