n, m = map(int, input().split())

if n>=2 and m>=2:
    print(n*m - (n-2)*2 - (m-2)*2 - 4)
elif n==1 and m==1:
    print(1)
elif n==1 and m>=2:
    print(m-2)
else:
    print(n-2)