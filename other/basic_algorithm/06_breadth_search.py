tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]

data = [0]  # start
while len(data) > 0:
    pos = data.pop(0)  # remove top
    print(pos, end='')
    for i in tree[pos]:
        data.append(i)  # nord od next search