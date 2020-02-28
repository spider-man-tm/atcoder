import random

# ３列並んだ時のパターン
goal = [
    0b111000000, 0b000111000, 0b000000111, 0b100100100,
    0b010010010, 0b001001001, 0b100010001, 0b001010100,
]

def check(player):
    for mask in goal:
        if player & mask==mask:
            return True
    return False


# 交互におく
def play(p1, p2):
    if check(p2):  # 3つ並んでいたら出力して終了
        print([bin(p1), bin(p2)])
        return

    board = p1 | p2  # 1(既に埋まっているマス目)を抽出
    if board==0b111111111: # すべて置いたら引き分けで終了
        print([bin(p1), bin(p2)])
        return

    # 置ける場所を探す(0のマス目をwに格納)
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    # ランダムに置く
    r = random.choice(w)
    play(p2, p1 | (1 << r))  # 攻守交代

play(0, 0)