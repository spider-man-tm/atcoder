k, a, b = map(int, input().split())

if b-a<=2 or a>k-1:
    print(k+1)
else:
    k -= a-1
    print(a + (b-a) * (k//2) + k %2)