N = int(input())
S = input()

w = S.count('.')
b = N - w
ans = min(w, b)
l, r = 0, w

for si in S:
    if si == '#':
        l += 1  # 現時点iも含め左側に存在する黒の数
    else:
        r -= 1  # 現時点iも含め右側に存在する白の数
    ans = min(ans, l+r)

print(ans)