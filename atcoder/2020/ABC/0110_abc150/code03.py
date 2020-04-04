import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

n_list = list(itertools.permutations(range(1, n+1)))

def func1(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

p_n = func1(n_list, p)
q_n = func1(n_list, q)

print(abs(p_n[0] - q_n[0]))