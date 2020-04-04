a, b, k = map(int, input().split())
ans = list(range(a, a+k)) + list(range(b-k+1, b+1))
ans = sorted(list(set(ans)))
for i in ans:
    if a <= i <= b:
        print(i)