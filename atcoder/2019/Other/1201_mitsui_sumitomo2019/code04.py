n = int(input())
s = input()
ans = 0

for i in range(1000):
    i = str(i).zfill(3)

    first = s.find(i[0])
    if first == -1:
        continue

    second = s.find(i[1], first+1)
    if second == -1:
        continue

    third = s.find(i[2], second+1)

    if third != -1:
        ans += 1

print(ans)