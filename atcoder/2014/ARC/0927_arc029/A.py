N = int(input())
T = [int(input()) for _ in range(N)]
T = sorted(T, reverse=True)

left, right = 0, 0

for t in T:
    if left<right:
        left += t
    else:
        right += t

print(max(left, right))