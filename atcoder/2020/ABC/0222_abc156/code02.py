n, k = map(int, input().split())

keta = 0
for i in range(10**10):
    ki = k**i
    if ki > n:
        print(keta)
        break
    else:
        keta += 1