n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
total = sum(m)
mini = min(m)
ans = n + (x-total)//mini
print(ans)