R, C, D = map(int, input().split())
A = []

if D==0:
    print(A[0][0])
    exit()

for _ in range(R):
    A.append(list(map(int, input().split())))

def check(n):
    w = n
    h = 0
    l = []
    while w >= 0:
        if w < C and h < R:
            l.append(A[h][w])
        w -= 1
        h += 1
    if l != []:
        return max(l)
    else:
        return 0

ans = 0
for i in range(D+1):
    if D%2==0:
        if i%2==0:
            ans = max(ans, check(i))
    else:
        if i%2==1:
            ans = max(ans, check(i))

print(ans)