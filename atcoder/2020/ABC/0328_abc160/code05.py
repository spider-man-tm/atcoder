X, Y, A, B, C = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)

eat_p = p[:X]
eat_q = q[:Y]
eat = sorted(eat_p + eat_q)

for i in range(min(len(eat), len(r))):
    if eat[i] < r[i]:   # 元々のリンゴより無色のリンゴの方が美味しい場合
        eat[i] = r[i]
    else:
        break

print(sum(eat))