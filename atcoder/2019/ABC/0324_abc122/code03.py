N, Q = map(int, input().split())
S = input()

total = [0]*(N+1)
for i in range(2, N+1):
    if S[i-2]=='A' and S[i-1]=='C':
        total[i] = total[i-1]+1
    else:
        total[i] = total[i-1]

for i in range(Q):
    l, r = map(int, input().split())
    print(total[r]-total[l])