n = input()
n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
n4 = int(n[3])
flag = False

for op1 in ['+', '-']:
    for op2 in ['+', '-']:
        for op3 in ['+', '-']:
            if op1 == '+':
                n12 = n1 + n2
            else:
                n12 = n1 - n2

            if op2 == '+':
                n23 = n12 + n3
            else:
                n23 = n12 - n3

            if op3 == '+':
                n34 = n23 + n4
            else:
                n34 = n23 - n4

            if n34 == 7:
                flag = True
                break
        if flag:
            break
    if flag:
        break

print(n1, op1, n2, op2, n3, op3, n4, '=7', sep='')