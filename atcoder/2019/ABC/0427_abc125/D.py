N = int(input())
A = list(map(int, input().split()))
abs_A = [abs(i) for i in A]

minus = 0
for i in range(N):
    minus += A[i] < 0

if minus % 2 == 0:
    print(sum(abs_A))
else:
    mini = float('inf')
    for i in range(N):
        mini = min(mini, abs_A[i])
    print(sum(abs_A) - 2*mini)
