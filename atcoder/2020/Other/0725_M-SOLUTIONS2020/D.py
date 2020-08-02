N = int(input())
A = list(map(int, input().split()))

A.append(0)
money = 1000

for i in range(N):
    if A[i] <= A[i+1]:
        kabu = money // A[i]
        money += (A[i+1] - A[i]) * kabu

print(money)