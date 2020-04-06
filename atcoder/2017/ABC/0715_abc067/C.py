n = int(input())
a = list(map(int, input().split()))

su = sum(a)
mini = 10**10
x = 0

for i in range(n-1):
    x += a[i]
    y = su - x
    diff = abs(x - y)

    if diff < mini:
        mini = diff

print(mini)