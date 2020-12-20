N, M, T = map(int, input().split())

E = N
now = 0

for _ in range(M):
    A, B = map(int, input().split())
    E -= A - now
    if E <= 0:
        print('No')
        exit()
    E += B - A
    E = min(N, E)
    now = B

E -= T - now

if E <= 0:
    print('No')
else:
    print('Yes')
