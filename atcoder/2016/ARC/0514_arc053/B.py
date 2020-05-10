from collections import Counter

S = list(input())
c = Counter(S)

odd_cnt = 0
for k, v in c.items():
    if v%2 == 1:
        odd_cnt += 1

if odd_cnt == 0:
    print(len(S))
else:
    cmb = (len(S)-odd_cnt) // 2
    ans = 1 + (cmb // odd_cnt)*2
    print(ans)