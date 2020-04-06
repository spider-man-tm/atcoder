n = int(input())

price = []

for i in range(1, 50000):
    p = int(i*1.08)
    price.append(p)

for i, p in enumerate(price):
    if p==n:
        print(i+1)
        exit()

print(':(')