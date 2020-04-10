N = int(input())
A = list(map(int, input().split()))

judge = 'reset'
cnt = 1

# judgeがresetに替わった際にcnt++
for i in range(N-1):
    if A[i] < A[i+1]:
        if judge == 'reset':
            judge = 'high'
        elif judge == 'low':
            judge = 'reset'
            cnt += 1
    elif A[i] > A[i+1]:
        if judge == 'reset':
            judge = 'low'
        elif judge == 'high':
            judge = 'reset'
            cnt += 1

print(cnt)