from math import ceil, floor
#ceil()  # 切り上げ。常にup
#floor()  # 切り捨て。常にdown
#int()  # 常に0に近く（正負で挙動違う）
#round(f),  round(f, 1)  # 四捨五入（第二引数で小数点桁数を指定）
n = int(input())
l = [int(input()) for _ in range(5)]
print(ceil(n / min(l)) + 4)