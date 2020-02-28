def honoi(n, src, dist, via):
    """
    src; 移動元
    dist; 移動先
    via; 経由場所
    """ 
    if n > 1:
        honoi(n-1, src, via, dist)  # n-1枚を経由場所に移動
        print(src, '->', dist)  # 最大の1枚を移動
        honoi(n-1, via, dist, src)  # n-1枚を移動先に移動
    else:
        print(src, '->', dist)

n = int(input())
honoi(n, 'a', 'b', 'c')