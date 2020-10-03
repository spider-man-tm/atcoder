N, X, T = map(int, input().split())

if N % X == 0:
    ans = N // X
else:
    ans = N // X + 1

print(T*ans) 