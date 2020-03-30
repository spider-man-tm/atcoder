n = int(input())
a = list(map(int, input().split()))

number = 1
count = 0
for num in a:
    if num==number:
        number += 1
    else:
        count += 1

if count==n:
    print(-1)
else:
    print(count)