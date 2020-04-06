n = int(input())
a1, a2, a3 = 0, 0, 1

if n<3:
    print(0)
    exit()

if n==3:
    print(1)
    exit()

for i in range(n-3):
    an = a1+a2+a3
    an %= 10007
    a3, a2, a1 = an, a3, a2

print(an)