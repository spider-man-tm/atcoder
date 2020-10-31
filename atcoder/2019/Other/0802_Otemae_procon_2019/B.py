M, N, K = map(int, input().split())
x = list(map(int, input().split()))

koma = [0] * (M+1)
for i in x:
    koma[i] += 1

ans = 0
for i in range(1, M+1):
    cnt = koma[i]
    for j in range(1, K+1):
        left = i-j
        right = i+j
        
        if left >= 0 and koma[left]:
            cnt += 1
        
        else:
            if right <= M and koma[right]:
                cnt += 1

    ans = max(ans, cnt)

print(ans)