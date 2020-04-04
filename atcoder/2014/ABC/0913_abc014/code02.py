n, x = map(int, input().split())
a = list(map(int, input().split()))

x = str(bin(x))[2:][::-1]
price = 0

for i in range(len(x)):
    flag = int(x[i])
    if flag:
        price += a[i]

print(price)