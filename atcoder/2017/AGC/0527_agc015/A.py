N, A, B = map(int, input().split())
maxi = A + B*(N-1)
mini = A*(N-1) + B
print(max(0, maxi-mini+1))