X = int(input())

eikaku = X if X < 180 else X - 180
cnt = 0

ans = 0
while True:
    ans += 1
    cnt += eikaku
    if cnt % 360 == 0:
        print(ans)
        break