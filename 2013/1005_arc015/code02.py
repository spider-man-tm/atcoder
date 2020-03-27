N = int(input())

def weather(M, m):
    w1 = M>=35
    w2 = M>=30 and M<35
    w3 = M>=25 and M<30
    w4 = m>=25
    w5 = M>=0 and m<0
    w6 = M<0
    return [w1, w2, w3, w4, w5, w6]

ans = [0, 0, 0, 0, 0, 0]
for _ in range(N):
    M, m = map(float, input().split())
    l = weather(M, m)
    ans[0] += l[0]
    ans[1] += l[1]
    ans[2] += l[2]
    ans[3] += l[3]
    ans[4] += l[4]
    ans[5] += l[5]

print(*ans)