n, k = map(int, input().split())
bunbo = n**3
bunshi = (k-1)*(n-k)*6 + (n-1)*3 + 1
print(bunshi/bunbo)