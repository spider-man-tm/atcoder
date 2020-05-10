X = int(input())

cnt = 0
m = 100
while True:
    m *= 1.01
    m = int(m)
    cnt += 1
    if m>=X:
        break

print(cnt)