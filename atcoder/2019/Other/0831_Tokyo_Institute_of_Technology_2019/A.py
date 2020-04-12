A, B, T = map(int, input().split())
diff = B-A

cnt = 0
while True:
    ans = B + cnt*diff
    if ans >= T:
        print(ans)
        exit()
    cnt += 1