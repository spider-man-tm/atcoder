n = int(input())
a = list(map(int, input().split()))

total = 0
for i in a:
    total += (1/i)

print(1/total)