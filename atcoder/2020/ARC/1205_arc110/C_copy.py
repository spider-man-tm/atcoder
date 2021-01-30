N = int(input())
P = list(map(int, input().split()))

ans = []
search = 0

for i in range(N):
    if P[i] == search + 1 or i == N - 1:
        P[search : i+1] = [search+1] + P[search : i]
        ans += list(range(i, search, -1))
        search = i

for i, j in zip(P, range(1, N+1)):
    if i != j:
        print(-1)
        exit()

print(*ans, sep='\n')
