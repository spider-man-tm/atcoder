N = int(input())
s = [input() for _ in range(5)]

for i in range(N):
    r1 = s[0][4*i:4*(i+1)]
    r2 = s[1][4*i:4*(i+1)]
    r3 = s[2][4*i:4*(i+1)]
    r4 = s[3][4*i:4*(i+1)]
    r5 = s[4][4*i:4*(i+1)]

    if r1=='.###':  #0,2,3,5,6,7,8,9
        if r2=='.#.#':  #0,8,9
            if r3=='.#.#':
                print(0, end='')
            else:  #8,9
                if r4=='.#.#':
                    print(8, end='')
                else:
                    print(9, end='')

        elif r2=='...#':  #2,3,7
            if r3=='...#':
                print(7, end='')
            else:
                if r4=='.#..':
                    print(2, end='')
                else:
                    print(3, end='')

        else:  #5,6
            if r4=='.#.#':
                print(6, end='')
            else:
                print(5, end='')

    else:  #1,4
        if r2=='.##.':
            print(1, end='')
        else:
            print(4, end='')