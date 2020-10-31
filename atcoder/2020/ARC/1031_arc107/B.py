N, K = map(int, input().split())

if K == 0:
    ans = N * N * 2
else:
    a = (K + 2) // 2
    b = (K + 2) - a
    print(a, b)
    tmp = N - b + 1
    print(tmp)
    tmp *= 2
    print(tmp)
    ans = tmp * 2 - 1 

print()
print(ans)