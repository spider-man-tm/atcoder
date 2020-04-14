N = int(input())
S = input()

n_R = S.count('R')
n_G = S.count('G')
n_B = N - n_R - n_G
ans = n_R * n_G * n_B

for i in range(N-2):
    for j in range(i+1, N-1):
        k = j + (j-i)
        if k < N:
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1

print(ans)