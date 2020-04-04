# atcoderではsympyは外部モジュール扱いで使用不可
from sympy import sieve, isprime

# 定義された範囲内から素数のリストを返す
print([i for i in sieve.primerange(1, 200)])

# 素数の判定
print(isprime(101))