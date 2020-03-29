n, k, m = map(int, input().split())
a = list(map(int, input().split()))

su = sum(a)

mokuh = n*m

last = mokuh - su

if k < last:
    print(-1)
elif last <= 0:
    print(0)
else:
    print(last)