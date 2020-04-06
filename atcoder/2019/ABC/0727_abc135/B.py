n = int(input())
p = list(map(int, input().split()))
p_sort = sorted(p)
non_0 = 0

for i in range(n):
    diff = p[i] - p_sort[i]
    if diff != 0:
        non_0 += 1
        if non_0 >2:
            print('NO')
            exit()

print('YES')