n = int(input())

def func(n):
    n -= 1
    if n // 20 % 2 == 0:
        print(n % 20 + 1)
    else:
        print(20 - (n % 20))

func(n)