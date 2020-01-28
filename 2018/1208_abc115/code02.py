n = int(input())
p = sorted([int(input()) for _ in range(n)])

p[-1] = p[-1]//2
print(int(sum(p)))