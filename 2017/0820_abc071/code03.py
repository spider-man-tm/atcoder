from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)  # リストの要素をカウント
cnt = [k for k, v in c.items() if v >= 2]

if len(cnt) < 2:
    print(0)
else:
    cnt = sorted(cnt, reverse=True)
    if c[cnt[0]] >= 4:
        print(cnt[0] * cnt[0])
    else:
        print(cnt[0] * cnt[1])