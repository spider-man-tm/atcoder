n,k=map(int,input().split())
lr=[list(map(int,input().split())) for _ in range(k)]
accum=[0]*k
dp=[0]*(n+1)
dp[1]=1
mod=998244353
for num in range(2,n+1):
    for i in range(k):
        l,r=lr[i]
        if l<num<=r:
            accum[i]+=dp[num-l]
            accum[i]%=mod
            dp[num]+=accum[i]
        elif r<num:
            accum[i]+=dp[num-l]-dp[num-r-1]
            accum[i]%=mod
            dp[num]+=accum[i]
        dp[num]%=mod
print(dp[n])
