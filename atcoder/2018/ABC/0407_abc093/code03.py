a, b, c = map(int, input().split())
vec = sorted([a, b, c])

ans = vec[2]-vec[1]
vec[0] += ans
vec[1] += ans

if (vec[1]-vec[0])%2==0:
    ans += (vec[1]-vec[0])//2
else:
    ans += (vec[1]-vec[0])//2+2

print(ans)