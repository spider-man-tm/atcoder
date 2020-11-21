X, Y, A, B = map(int, input().split())

cnt = 0
while True:
    kakomon_A = X * A
    atcoder_A = X + B
    if kakomon_A < atcoder_A:
        if kakomon_A > Y:
            print(cnt)
            exit()
        else:
            X = kakomon_A
            cnt += 1
    else:
        if atcoder_A > Y:
            print(cnt)
            exit()
        else:
            diff = Y - X
            cnt += (diff-1) // B
            print(cnt)
            exit()
