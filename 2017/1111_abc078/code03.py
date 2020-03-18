n, m = map(int, input().split())

pro = (1/2)**m
time = (n-m)*100 + m*1900

ans = int(time*(1/pro))
print(ans)