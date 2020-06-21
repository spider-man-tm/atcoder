N, K = map(int, input().split())
ans = True
t1 = int(input())
t2 = int(input())
t3 = 0

for i in range(N-2):
    t3 = int(input())
    if t1+t2+t3 < K:
        ans = False
        break
    else:
        t1, t2 = t2, t3

if ans:
    print(-1)
else:
    print(i+3)