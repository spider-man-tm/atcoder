S = list(input())
N = len(S)
pre = '#'
now = ''
cnt = 0

for i in range(N):
    now += S[i]
    # print('pre: ', pre)
    # print('now: ', now)
    if now != pre:
        cnt += 1
        pre = now
        now = ''
    # print('cnt: ', cnt)
    # print()

print(cnt)