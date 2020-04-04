tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]

data = [0]
while len(data) > 0:
    pos = data.pop() # last number
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)

# 0 2 6 14 13 5 12 11 1 4 10 9 3 8 7