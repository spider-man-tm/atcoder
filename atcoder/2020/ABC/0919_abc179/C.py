N = int(input())
ans = 0

for i in range(1, N):
    if i >= N:
        break

    for j in range(1, N):
        tmp = i * j

        if tmp >= N:
            break

        ans += 1

print(ans)