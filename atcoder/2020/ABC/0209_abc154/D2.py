N, K = map(int, input().split())
p = [(1+i)/2 for i in list(map(int, input().split()))]

ans = sum(p[:K])
sums = ans
start = 0

for i in range(K, N):
    sums += p[i]
    sums -= p[start]
    ans = max(ans, sums)
    start += 1
    
print(ans)