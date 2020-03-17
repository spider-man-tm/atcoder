from collections import Counter as C
n = int(input())
V = list(input().split())

V1 = C(V[::2]).most_common()
V2 = C(V[1::2]).most_common()

if V1[0][0] != V2[0][0]:
  ans = n - (V1[0][1] + V2[0][1])
  
else:
  l = V1[0][1] + V2[1][1] if len(V2) > 1 else V1[0][1]
  r = V1[1][1] + V2[0][1] if len(V1) > 1 else V2[0][1]

  if l >= r:
    ans = n - l
  else:
    ans = n - r

print(ans)