import bisect
 
N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()
 
sum1 = [H[i + 1] - H[i] for i in range(N - 1)]
sum2 = sum1[1::2] + [0]
sum1 = [0] + sum1[::2]
for i in range(len(sum1) - 1):
    sum1[i + 1] += sum1[i]
for i in range(len(sum2) - 1, 0, -1):
    sum2[i - 1] += sum2[i]
 
ans = 1 << 60
 
for w in W:
    x = bisect.bisect(H, w)
    if x % 2:
        x -= 1
    cost = sum1[x // 2] + sum2[x // 2] + abs(H[x] - w)
    if ans > cost:
        ans = cost
 
print(ans)
