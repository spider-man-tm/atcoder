from bisect import bisect_left, bisect_right  # return index

N = int(input())
L = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        tmp = L[i]+L[j]  # tmpはこの値より短くなくてはいけない

        ### ここから下は二分探索
        ix = bisect_left(L, tmp)
        ans += ix-(j+1)

print(ans)