H, W = map(int, input().split())
masu = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]

# スタート地点が黒の場合、始めからカウント1が追加される
if masu[0][0] == '#':
    dp[0][0] = 1

for i in range(H):
    for j in range(W):
        # i=0（1行目）は上から進入することは付加
        # よってa（上の行からきた場合のコスト）はfloatと仮置き
        if i==0:
            a = float('inf')
            pr = 'koko1'
        else:
            # 白から黒に切り替わった場合、+1
            if masu[i][j]=='#' and masu[i-1][j]=='.':
                a = dp[i-1][j] + 1
                pr = 'koko2'
            # 色が連続していたり、黒から白に変わった場合はカウントなし
            else:
                a = dp[i-1][j]
                pr = 'koko3'
        # j=0（1列目）は左から進入することは付加
        # よってb（左の列からきた場合のコスト）はfloatと仮置き
        if j==0:
            b = float('inf')
            pr += 'koko4'
        else:
            # 白から黒に切り替わった場合、+1
            if masu[i][j]=="#" and masu[i][j-1]==".":
                b = dp[i][j-1] + 1
                pr += 'koko5'
            # 色が連続していたり、黒から白に変わった場合はカウントなし
            else:
                b = dp[i][j-1]
                pr += 'koko6'
        if a!=float('inf') or b!=float('inf'):
            dp[i][j] = min(a, b)

        print(pr, a, b)
        print(dp)
    
print()
print(dp)