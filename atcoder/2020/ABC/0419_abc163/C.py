N = int(input())
A = list(map(int, input().split()))

P = [[] for _ in range(N)]
for i in range(N-1):
    jousi = A[i]-1
    P[jousi].append(i+1)

for v in P:
    print(len(v))