Q, H, S, D = map(int, input().split())   # 0.25, 0.5, 1.0, 2.0
N = int(input())

if N%2==0:
    kijun1 = min(Q*8, H*4, S*2, D)
    print(N//2 * kijun1)
else:
    kijun1 = min(Q*8, H*4, S*2, D)
    kijun2 = min(Q*4, H*2, S)
    print(N//2 * kijun1 + kijun2)