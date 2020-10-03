N, S = input().split()
N = int(N)

cnt = 0
for i in range(N):
    c1, c2 = 0, 0
    for j in range(i, N):
        if S[j] == 'A':
            c1 += 1
        elif S[j] == 'T':
            c1 -= 1
        elif S[j] == 'C':
            c2 += 1
        else:
            c2 -= 1
        
        if not c1 and not c2:
            cnt += 1

print(cnt)