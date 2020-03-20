n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

if n >= m:
    print(0)
    exit()

diff = sorted([x[i+1] - x[i] for i in range(m-1)], reverse=True)
print(sum(diff[n-1:]))