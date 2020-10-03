N = int(input())

coin = set()

for _ in range(N):
    A, B = map(int, input().split())
    coin.add((min(A, B), max(A, B)))

print(len(coin))