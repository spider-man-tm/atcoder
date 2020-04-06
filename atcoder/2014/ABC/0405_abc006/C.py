N, M = map(int, input().split())

# Mが取りうる可能な範囲  2*N ~ 3*N ~ 4*N
if M<2*N or 4*N<M:
    print(-1, -1, -1)
    exit()

if M<=3*N:
    tmp = M-2*N
    print(N-tmp, tmp, 0)
    exit()

else:
    tmp = M-3*N
    print(0, N-tmp, tmp)