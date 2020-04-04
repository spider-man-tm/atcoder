def fibonacci(n):
    """
    フィボナッチ数列のn番目を返す関数
    再帰処理
    """
    if (n==1) or (n==2):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(16))


memo = {1: 1, 2: 1}
def fibonacci_memo(n):
    """
    メモ化を行うことで処理が高速になる
    """
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-2) + fibonacci(n-1)
    return memo[n]

print(fibonacci(16))