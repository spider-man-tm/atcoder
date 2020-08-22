def func(n):
    if n == 0:
        return 100
    elif n == 1:
        return 100
    elif n == 2:
        return 200
    else:
        return func(n-1) + func(n-2) + func(n-3)

print(func(19))