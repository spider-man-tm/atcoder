data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    #print('data: ', data)
    if not change:
        break
    change = False
    for j in range(len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            change = True

print(data)

"""
data:  [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
data:  [6, 4, 2, 8, 5, 11, 9, 7, 13, 15]
data:  [4, 2, 6, 5, 8, 9, 7, 11, 13, 15]
data:  [2, 4, 5, 6, 8, 7, 9, 11, 13, 15]
data:  [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
data:  [2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
[2, 4, 5, 6, 7, 8, 9, 11, 13, 15]
"""