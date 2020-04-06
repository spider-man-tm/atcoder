n = int(input())
ans = list(input())

for i in range(n - 1):
    s = list(input())
    tmp = []
    for i in range(len(s)):
        if s[i] in ans:
            tmp.append(s[i])  # 共通の文字はtmpに追加
            ans.remove(s[i])  # 追加した文字はansから削除
    ans = tmp

ans.sort()
print(''.join(ans))