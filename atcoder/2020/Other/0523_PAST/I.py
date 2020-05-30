N = int(input())
Q = int(input())

row = list(range(N))
col = list(range(N))

flag = True

for _ in range(Q):
    query = input().split()
    if query[0]=='1':
        a, b = int(query[1])-1, int(query[2])-1
        if flag:
            row[a] = b
            row[b] = a
        else:
            col[a] = b
            col[b] = a
    elif query[0]=='2':
        a, b = int(query[1])-1, int(query[2])-1
        if flag:
            col[a] = b
            col[b] = a
        else:
            row[a] = b
            row[b] = a
    elif query[0]=='3':
        flag = not flag
    else:
        a, b = int(query[1])-1, int(query[2])-1
        p_r = row[a]
        p_c = col[b]

        print(N*(p_r)+p_c)