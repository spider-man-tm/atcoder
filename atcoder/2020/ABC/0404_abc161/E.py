N, K, C = map(int, input().split())
S = list(input())
rS = S[::-1]
lcnt, rcnt = 0, 0
left, right = [0]*N, [0]*N
llimit, rlimit = -1, -1

for i in range(N):
    # 左から貪欲
    # llimit (数字がカウントされた日+C日)以降
    # 上記かつ、シフトに入れる日 ('o')であればシフトに入る。
    if S[i] == 'o' and llimit<i:
        lcnt += 1
        left[i] = lcnt
        llimit = i + C

    # 右から貪欲
    if rS[i] == 'o' and rlimit<i:
        rcnt += 1
        right[-(i + 1)] = K + 1 - rcnt
        rlimit = i + C

#print(left)
#print(right)

# leftとrightで同じ数字が入っている日にちを出力
for i in range(N):
    if left[i]==right[i] and left[i]>0:
        print(i + 1)