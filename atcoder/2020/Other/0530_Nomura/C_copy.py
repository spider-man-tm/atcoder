N = int(input())
A = list(map(int, input().split()))

pm = sum(A)
e, total_e = 1, 1

for i in A:
    pm -= i
    e = min((e-i) * 2, pm)
    if e < 0:
        break
    total_e += e

    print('i: ', i)
    print('pm: ', pm)
    print('e: ', e)
    print()

if e < 0:
    print(-1)
else:
    print(total_e)