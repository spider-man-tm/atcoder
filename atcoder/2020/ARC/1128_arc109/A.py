a, b, x, y = map(int, input().split())

dpA = [0]*101
dpB = [0]*101

cntA = 0
cntB = x
for i in range(a, 101):
    dpA[i] = cntA
    dpB[i] = cntB
    cntA += min(2*x, y)
    cntB += min(2*x, y)

cntA = 0
for i in range(a, -1, -1):
    dpA[i] = cntA
    cntA += min(2*x, y)

cntB = x
for i in range(a-1, -1, -1):
    dpB[i] = cntB
    cntB += min(2*x, y)

print(dpB[b])
