n = int(input())
a = list(map(int, input().split()))
ans = [0] * (10**5+3)

for i in range(n):
    mini, mid, maxi = a[i], a[i]+1, a[i]+2
    ans[mini] += 1;  ans[mid] += 1;  ans[maxi] += 1

print(max(ans))