N = int(input())
A = list(map(int, input().split()))
Q = int(input())

numbers = [0] * (10**5+2)
total = sum(A)

for a in A:
    numbers[a] += 1

for _ in range(Q):
    B, C = map(int, input().split())
    tmp = numbers[B]
    #print('tmp: ', tmp)
    diff = (C-B) * tmp
    #print('diff: ', diff)
    total += diff
    numbers[B] = 0
    numbers[C] += tmp
    print(total)
    #print()