s = input()
res, ans = 0, 0

for i in s:
    if i in ['A', 'C', 'G', 'T']:
        res += 1   # 指定した文字列がどれだけ連続しているか
    else:
        ans = max(res, ans)
        res = 0    # 文字列の連続が途切れた場合、0にリセット

ans = max(res, ans)
print(ans)