N, K = map(int, input().split())
sunuke = [0]*N

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        sunuke[a-1] += 1

print(sunuke.count(0))