N = 8

# 斜めのチェック
def check(x, col):
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row):
            return False
    return True

def search(col):
    if len(col) == N:
        print(col)
        return

    for i in range(N):
        if i not in col:
            if check(i, col):
                col.append(i)
                search(col)
                col.pop()

search([])