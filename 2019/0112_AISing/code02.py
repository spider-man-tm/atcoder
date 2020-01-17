n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

first = 0
second = 0
third = 0

for i in p:
    if i<=a:
        first += 1
    elif i<=b:
        second += 1
    else:
        third += 1

print(min(first, second, third))