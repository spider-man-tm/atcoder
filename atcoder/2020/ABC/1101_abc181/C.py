from itertools import combinations

N = int(input())

san = []
for _ in range(N):
    x, y = map(int, input().split())
    san.append([x, y])

def check(ss):
    ss = sorted(ss)
    x1 = ss[0][0]
    x2 = ss[1][0]
    x3 = ss[2][0]
    y1 = ss[0][1]
    y2 = ss[1][1]
    y3 = ss[2][1]
    if x1 == x3:
        if x1 == x2:
            return True
        else:
            return False
    if x1 == x2:
        if x1 == x3:
            return True
        else:
            return False
    if y1 == y3:
        if y1 == y2:
            return True
        else:
            return False
    if y1 == y2:
        if y1 == y3:
            return True
        else:
            return False

    tmp2 = (y3 - y1) / (x3 - x1)
    tmp1 = (y2 - y1) / (x2 - x1)
    if tmp2 == tmp1:
        return True
    else:
        return False

for i, j, k in combinations(range(N), 3):
    s1 = san[i]
    s2 = san[j]
    s3 = san[k]
    
    if check([s1, s2, s3]):
        print('Yes')
        exit()
    
print('No')