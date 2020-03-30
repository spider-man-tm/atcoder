N = int(input())
buka = [[] for _ in range(N)]

for i in range(1, N):
    b = int(input())-1
    buka[b].append(i)

def salary(x):
    if not buka[x]:
        return 1
    l = [salary(i) for i in buka[x]]
    return max(l) + min(l) + 1

print(salary(0))