N = int(input())
A = list(map(int, input().split()))
A = list(reversed(sorted(A)))
new_A = []
for i in range(1, N//2+1):
    new_A.append(A[i])
    new_A.append(A[i])

new_A = [0] + [A[0]] + new_A

print(sum(new_A[:N]))