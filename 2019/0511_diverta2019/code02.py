R, G, B, N = map(int, input().split())

ans = 0
n_iter_r = N//R + 1
n_iter_g = N//G + 1

for r in range(n_iter_r):
    for g in range(n_iter_g):
        nokori = N - R*r - G*g
        if nokori < 0:
            break
        else:
            if nokori%B==0:
                ans += 1

print(ans)