data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    temp = data[i]
    j = i-1
    while (j>=0) and (data[j]>temp):
        print('ソート発生!')
        data[j+1] = data[j]
        j -= 1
    data[j+1] = temp
    print('data: ', data)
    
    """
    data:  [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    ソート発生!
    ソート発生!
    data:  [4, 6, 15, 2, 8, 5, 11, 9, 7, 13]
    ソート発生!
    ソート発生!
    ソート発生!
    data:  [2, 4, 6, 15, 8, 5, 11, 9, 7, 13]
    ソート発生!
    data:  [2, 4, 6, 8, 15, 5, 11, 9, 7, 13]
    ソート発生!
    ソート発生!
    ソート発生!
    data:  [2, 4, 5, 6, 8, 15, 11, 9, 7, 13]
    ソート発生!
    data:  [2, 4, 5, 6, 8, 11, 15, 9, 7, 13]
    ソート発生!
    ソート発生!
    data:  [2, 4, 5, 6, 8, 9, 11, 15, 7, 13]
    ソート発生!
    ソート発生!
    ソート発生!
    ソート発生!
    data:  [2, 4, 5, 6, 7, 8, 9, 11, 15, 13]
    ソート発生!
    data:  [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
    """

print(data)