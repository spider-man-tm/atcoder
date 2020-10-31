N = int(input())
p = list(map(int, input().split()))

kishutu = [0] * 200001
ans = 0

for i in p:
    kishutu[i] += 1
    while kishutu[ans]:
        ans += 1

    print(ans)