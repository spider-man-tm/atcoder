data = [3, 4, 1, 8, 8, 0, 3, 8, 9, 3, 2, 7, 4, 5]


def bin_sort(data):
    """ dataは 0~9 の値に限定 """
    _list = [0 for _ in range(10)]
    
    for i in data:
        _list[i] += 1

    return_data = []
    for i, n in enumerate(_list):
        for _ in range(n):
            return_data.append(i)

    return return_data


print(bin_sort(data))