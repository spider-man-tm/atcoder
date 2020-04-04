b = list(map(int, input().split()))
N = int(input())

def num_trans(n):
    n = str(n)
    nn = ''
    for i in n:
        ii = b.index(int(i))
        nn += str(ii)
    return int(nn)


def num_reverse(n):
    n = str(n)
    nn = ''
    for i in n:
        ii = b[int(i)]
        nn += str(ii)
    return int(nn)

a = sorted([num_trans(int(input())) for _ in range(N)])

for i in a:
    print(num_reverse(i))