N = int(input())
A = list(map(int, input().split()))

left = max(A[:2**(N-1)])
right = max(A[2**(N-1):])

ans = min(left, right)

print(A.index(ans) + 1)