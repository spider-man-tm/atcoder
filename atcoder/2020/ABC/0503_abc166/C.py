N, M = map(int, input().split())
H = list(map(int, input().split()))

HH = [True]*N

for _ in range(M):
    A, B = map(int, input().split())
    if H[A-1] <= H[B-1]:
        HH[A-1] = False
    if H[A-1] >= H[B-1]:
        HH[B-1] = False

print(HH.count(True))