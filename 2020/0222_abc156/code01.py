n, r = map(int, input().split())

if n<10:
    kasan = 100 * (10-n)
    print(r+kasan)

else:
    print(r)