N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]

maxi = max(S)
mini = min(S)

if maxi==mini:
    print(-1)
    exit()
    
P = B/(maxi-mini)

for i in range(N):
    S[i] = S[i]*P

mean = sum(S)/N
Q = A - mean

print(P, Q)