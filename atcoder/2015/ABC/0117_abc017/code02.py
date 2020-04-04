s = input()
c_flag = False

for i in s:
    if c_flag == False:
        if i!='o' and i!='k' and i!='u':
            if i!='c':
                print('NO')
                exit()
            else:
                c_flag = True
    else:
        if i!= 'h':
            print('NO')
            exit()
        else:
            c_flag = False

print('YES')