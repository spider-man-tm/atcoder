N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if is_prime(N):
    print('YES')
else:
    print('NO')