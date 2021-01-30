N = int(input())

ans = [[] for _ in range(N)]
ans[0] = 'a'

for i in range(1, N):
    for c in ans[i-1]:
        maxi = max([ord(cc) for cc in c])
        for j in range(97, maxi+2):
            ans[i].append(c + chr(j))

for s in ans[-1]:
    print(s)
