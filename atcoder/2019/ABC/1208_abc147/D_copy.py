import numpy as np

mod = 10**9+7

N = int(input())
A = np.array(list(map(int, input().split())))

ans = 0

# max(A)を2進数表記した時の桁数
for n in range(len(bin(max(A)))-2):
    #print(A >> n)   # Aの各値をnだけ右シフトした数（2で割っていく）
    #print((A >> n) & 1)

    # (n+1)桁目が1である数字がAにどれくらいあるか
    n_1 = np.count_nonzero((A >> n)&1)
    n_0 = N - n_1   # (n+1)桁目が0である数字がAにどれくらいあるか

    #print(n_1)
    #print(n_0)
    #print()

    ans += ((2**n)*n_1*n_0) % mod

print(ans%mod)