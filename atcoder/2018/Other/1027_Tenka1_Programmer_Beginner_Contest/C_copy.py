N = int(input())
A = [int(input()) for _ in range(N)]
A = sorted(A)
half = (N+1)//2

if N%2==0:
    mini = A[:half]
    maxi = A[half:]
    ans = 2*(sum(maxi)-sum(mini)) - maxi[0] + mini[-1]
    print(ans)
else:
    mini = A[:half-1]
    maxi = A[half-1:]
    ans1 = 2*(sum(maxi)-sum(mini)) - maxi[0] - maxi[1]

    mini = A[:half]
    maxi = A[half:]
    ans2 = 2*(sum(maxi)-sum(mini)) + mini[-1] + mini[-2]

    print(max(ans1, ans2))