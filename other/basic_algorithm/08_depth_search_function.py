tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]


def search(pos):
    """行きがけ順"""
    print(pos, end=' ')  # 親ノード
    for i in tree[pos]:
        search(i)  # 再帰的処理（func in func）

search(0)
# 0 1 3 7 8 4 9 10 2 5 11 12 6 13 14


def search(pos):
    """帰りがけ順"""
    for i in tree[pos]:
        search(i)
    print(pos, end=' ')

search(0)
# 7 8 3 9 10 4 1 11 12 5 13 14 6 2 0


def search(pos):
    """通りがけ順"""
    if len(tree[pos]) == 2:
        search(tree[pos][0])
        print(pos, end=' ')
        search(tree[pos][1])
    elif len(tree[pos]) == 1:
        search(tree[pos][0])
        print(pos, end=' ')
    else:
        print(pos, end=' ')

search(0)
# 7 3 8 1 9 4 10 0 11 5 12 2 13 6 14