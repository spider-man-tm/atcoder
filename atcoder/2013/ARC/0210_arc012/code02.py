N, va, vb, L = map(int, input().split())

for _ in range(N):
    t = L/va
    L = vb*t

print(round(L, 10))