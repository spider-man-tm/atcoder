N, Q = map(int, input().split())
A = list(map(int, input().split()))

bit = [0] * (N+1)
for i in range(N):
    bit[i+1] = bit[i] ^ A[i]

print(bit)

for _ in range(Q):
    T, X, Y = map(int, input().split())
    
    if T == 1:
        #A[X-1] ^= Y
        bit[X-1] ^= Y
    else:
        print(bit[X] ^ bit[Y])
