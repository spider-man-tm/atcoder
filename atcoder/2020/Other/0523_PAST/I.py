N = int(input())
rows = [i for i in range(N)]
columns = [i for i in range(N)]
transposed = False

Q = int(input())
for _ in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 3:
        transposed = not transposed
    else:
        A, B = q[1]-1, q[2]-1
        if q[0] == 1:
            if transposed:
                columns[A], columns[B] = columns[B], columns[A]
            else:
                rows[A], rows[B] = rows[B], rows[A]
        elif q[0] == 2:
            if transposed:
                rows[A], rows[B] = rows[B], rows[A]
            else:
                columns[A], columns[B] = columns[B], columns[A]
        elif q[0] == 4:
            if transposed:
                A, B = B, A
            r,c = rows[A], columns[B]

            print(N*r+c)