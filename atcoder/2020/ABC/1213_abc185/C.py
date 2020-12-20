L = int(input())

N = L - 1

from scipy.special import comb

print(comb(N, 11, exact=True))
