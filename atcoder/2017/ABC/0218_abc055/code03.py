n, m = map(int, input().split())

if 2*n == m:
    print(n)

elif 2*n < m:
    ans = n + (m-2*n)//4
    print(ans)

else:
    ans = m//2
    print(ans)