N, D, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(D)]
ST = [list(map(int, input().split())) for _ in range(K)]

for s, t in ST:
    now = s
    day = 0
    for l, r in LR:
        day += 1
        if now < t:
            if l <= now <= r:
                now = r
            if t <= now:
                break   # ここで目的地到着
        
        else:
            if l <= now <= r:
                now = l
            if t >= now:
                break   # ここで目的地到着
    
    print(day)