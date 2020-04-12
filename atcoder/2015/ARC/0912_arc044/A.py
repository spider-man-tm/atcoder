N = int(input())

def digsum(n):
    total = 0
    while n > 0:
        total += n%10
        n /= 10
        n = int(n)
    return total

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_prime2(n):
    if n == 1:
        return False
    if is_prime(n):
        return True
    else:
        t = n%10
        if t%2 != 0 and t != 5:
            if digsum(n)%3 != 0:
                return True
            else:
                return False
        else:
            return False

if is_prime2(N):
    print('Prime')
else:
    print('Not Prime')