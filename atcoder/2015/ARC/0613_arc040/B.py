N, R = map(int, input().split())
S = list(input())

n_idou = 0
for i, s in enumerate(S[::-1]):
    if s=='.':
        n_idou = max(N-i-R, 0)
        break

n_shot = 0
i = 0
while i<N:
    if S[i]=='.':
        S[i:i+R] = ['o']*R
        n_shot += 1
    i += 1

print(n_idou+n_shot)