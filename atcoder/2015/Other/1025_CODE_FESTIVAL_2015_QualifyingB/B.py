N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] * (M+1)

for i in range(N):
    ans[A[i]] += 1

if max(ans) > N // 2:
    print(ans.index(max(ans)))
else:
    print('?')