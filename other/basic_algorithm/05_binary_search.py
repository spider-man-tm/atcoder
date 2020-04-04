def binary_search(data, value):
    """dataはsortされていることが条件"""
    left = 0
    right = len(data) - 1
    while left <= right:
        print('left: ', left)
        print('right: ', right)
        mid = (left + right) // 2
        print('mid: ', mid, '\n')
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左をセンターに
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右をセンターに
            right = mid - 1
    # 見つからない場合-1をreturn
    return -1

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(data, 6))

"""
left:  0
right:  9
mid:  4 

left:  5
right:  9
mid:  7 

left:  5
right:  6
mid:  5 

left:  6
right:  6
mid:  6 

6
"""