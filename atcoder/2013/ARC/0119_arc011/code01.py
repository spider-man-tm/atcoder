m, n, N = map(int, input().split())
ans = 0
add = N
mod = 0

while add+mod>=m:
    ans += add
    mod += add
    add = mod//m * n
    mod = mod%m

print(ans+add)