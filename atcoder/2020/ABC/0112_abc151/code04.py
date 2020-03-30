from collections import deque
import numpy as np

H, W = map(int,input().split())
S = [list(input()) for _ in range(H)]

ans = 0
for i in range(H):
  for j in range(W):

    if S[i][j]=='#':
      continue
    
    # A[i][j]をスタート位置に設定
    # スタート以外は一旦無限数に設定
    inf = 10**5
    A = [[inf]*W for _ in range(H)]
    A[i][j]=0

    # スタート位置をキューに追加
    q = deque([[i, j]])

    # 全てのマスを探索するまでwhile
    while q:
      a = q.popleft()
      x=a[0]
      y=a[1]
      b = A[x][y]
      for h, w in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        
        # マスが範囲外の場合
        if (h<0) or (h>H-1) or (w<0) or (w>W-1):
          continue
        # マスが障害物の場合
        if S[h][w]=='#':
          continue

        # すでに距離が確定しているマスに＋１を追加した数
        c = b+1

        # cが無限大（未探索）より大きい場合、continue
        if c>=A[h][w]:
          continue

        A[h][w]=c
        # 探索済みのマスをキューに追加
        q.append([h,w])
      
    A = np.array(A)

    # 未到達のマス以外で最も距離が長いマスの距離
    # 前回までのansと上記の数を比べて大きい方をansに代入
    ans = max(ans, max(A[A<10**5]))
    
print(ans)