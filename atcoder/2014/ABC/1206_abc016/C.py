n, m = map(int, input().split())
friend = [[100 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    friend[a][b] = 1
    friend[b][a] = 1

for i in range(n):
    friend[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            friend[i][j] = min(friend[i][j], friend[i][k]+friend[k][j])
            # ダイクストラ法
            # iからjに直接行くよりもkを経由した方が近い場合、iとjの距離を更新

for m in range(n):
    print(friend[m].count(2))
    # 最終的に距離が2の関係がいくつあるかを出力