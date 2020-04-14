N = int(input())
S = list(input())

num_r = S.count('R')
num_g = S.count('G')
num_b = N - num_r - num_g
C = [[num_r, num_g, num_b] for _ in range(N)]
r_cnt, g_cnt, b_cnt = 0, 0, 0

for i in range(N):
    if S[i] == 'R':
        r_cnt += 1
    elif S[i] == 'G':
        g_cnt += 1
    else:
        b_cnt += 1

    C[i][0] -= r_cnt
    C[i][1] -= g_cnt
    C[i][2] -= b_cnt

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        if S[i] != S[j]:
            if 'R' not in [S[i], S[j]]:
                ans += C[j][0]
                if j+(j-i) < N and S[j+(j-i)]=='R':
                    ans -= 1
            if 'G' not in [S[i], S[j]]:
                ans += C[j][1]
                if j+(j-i) < N and S[j+(j-i)]=='G':
                    ans -= 1
            if 'B' not in [S[i], S[j]]:
                ans += C[j][2]
                if j+(j-i) < N and S[j+(j-i)]=='B':
                    ans -= 1

print(ans)