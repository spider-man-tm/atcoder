N = input()

def digsum(n):
    total = 0
    while n > 0:
        total += n%10
        n /= 10
        n = int(n)
    return total

if len(N)==1:
    print(N)
    exit()

if N[1:].count('9') == len(N)-1:
    print(digsum(int(N)))
    exit()

ans = int(str(int(N[0])-1) + '9'*(len(N)-1))
print(digsum(ans))