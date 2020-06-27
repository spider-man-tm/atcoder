N, M = map(int, input().split())

if M > N:
    print('NO')
    exit()

A = list(reversed(sorted(list(map(int, input().split())))))
B = list(reversed(sorted(list(map(int, input().split())))))

for i in range(M):
    if B[i] > A[i]:
        print('NO')
        exit()

print('YES')