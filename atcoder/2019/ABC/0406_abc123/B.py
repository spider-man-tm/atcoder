import itertools

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

dish = [a, b, c, d, e]
ans = 1000

def return_time(t):
    time = t//10 * 10
    mod = t%10
    if mod != 0:
        time += 10
    return time

for v in itertools.permutations(dish, 5):
    t1, t2, t3, t4, t5 = v[0], v[1], v[2], v[3], v[4]
    total = 0
    for t in [t1, t2, t3, t4]:
        total += return_time(t)
    total += t5
    ans = min(ans, total)

print(ans)