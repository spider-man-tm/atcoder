N, K = map(int, input().split())
P = list(map(int, input().split()))
P = sorted(P)

print(sum(P[:K]))