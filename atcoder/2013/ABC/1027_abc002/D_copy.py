from itertools import combinations

N, M = map(int, input().split())
R = [tuple(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(2**N):
    members = [j+1 for j in range(N) if (i>>j)&1 == 1]
    #print('members: ', members)
    num = len(members)

    tmp = all(tuple(x) in R for x in combinations(members, 2)) and num
    ans = max(ans, tmp)
    
print(ans)