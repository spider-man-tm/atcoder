K, T = map(int, input().split())
A = list(map(int, input().split()))

max_at = max(A)
print(max(max_at-1 - (K-max_at), 0))