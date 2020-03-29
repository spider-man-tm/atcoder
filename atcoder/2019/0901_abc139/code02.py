a, b = map(int, input().split())

a -= 1
c = 1

count = 0

while c < b:
    count += 1
    c += a

print(count)