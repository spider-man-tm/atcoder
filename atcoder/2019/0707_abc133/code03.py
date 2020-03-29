l, r = map(int, input().split())

ans = 2019
end_flag = False

for i in range(l, r):
    for j in range(i+1, r+1):
        mod = (i*j)%2019
        if mod < ans:
            ans = mod

        if ans==0:
            end_flag = True
            break

    if end_flag:
        break

print(ans)