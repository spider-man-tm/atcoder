city = [0, 0, 0, 0]
for _ in range(3):
    a, b = map(int, input().split())
    city[a-1] += 1
    city[b-1] += 1

if max(city)==2 and min(city)==1:
    print('YES')
else:
    print('NO')