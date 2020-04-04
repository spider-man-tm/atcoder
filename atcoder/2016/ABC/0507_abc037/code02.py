n, q = map(int, input().split())
ans = [0] * n

for _ in range(q):
    l, r, t = map(int, input().split())
    ans[l-1:r] = [t] * (r-l+1)

for i in ans:
    print(i)