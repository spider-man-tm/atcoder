N, P = map(int, input().split())
A = list(map(int, input().split()))
L = [i%2 for i in A]

odd_cnt = L.count(1)
eve_cnt = L.count(0)

if odd_cnt == 0:
    if P == 0:
        print(2**N)
    else:
        print(0)
else:
    print(2**(N-1))