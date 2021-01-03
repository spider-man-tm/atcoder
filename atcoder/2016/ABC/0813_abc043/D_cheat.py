def check2(x):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return f'{i+1} {i+2}'
    return False


def check3(x):
    for i in range(len(x)-2):
        if x[i] == x[i+2]:
            return f'{i+1} {i+3}'
    return False


s = input()
c2 = check2(s)
c3 = check3(s)

print(c2 or c3 or '-1 -1')