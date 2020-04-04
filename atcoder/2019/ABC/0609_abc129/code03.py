N, M = map(int, input().split())
A = set([int(input()) for _ in range(M)])
mod = 10**9+7

step = [0] * (N+1)
step[0] = 1
step[1] = 1

for i in range(N+1):
    if i==0 or i==1:
        if i in A:
            step[i] = 0
    else:
        step[i] = step[i-1]+step[i-2]
        if i in A:
            step[i] = 0
        step[i] %= mod

print(step[-1])