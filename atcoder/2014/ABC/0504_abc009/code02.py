n = int(input())
dish = []
for _ in range(n):
    dish.append(int(input()))

dish = sorted(list(set(dish)))
print(dish[-2])