N, A, B = map(int, input().split())
S = input()

total_AB, total_B = 0, 0
for c in S:
    if c=='a':
        if total_AB < A+B:
            print('Yes')
            total_AB += 1
        else:
            print('No')
    elif c=='b':
        if total_AB < A+B and total_B < B:
            print('Yes')
            total_AB += 1
            total_B += 1
        else:
            print('No')
    else:
        print('No')