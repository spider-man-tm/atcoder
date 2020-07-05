from bisect import bisect_left, bisect_right  # return index


N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0

for i in range(N):
    b = B[i]
    a_ix = bisect_left(A, b)
    c_ix = bisect_right(C, b)
    ans += a_ix * (N - c_ix)

print(ans)