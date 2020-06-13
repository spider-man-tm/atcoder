def check_perfect(n):
    n_sqrt = int(n**0.5)
    total = 1
    for i in range(2, n_sqrt+1):
        if n%i == 0:
            total += i
            total += n//i
    
    if n_sqrt**2 == n:
        total -= n_sqrt

    if total == n:
        return 'Perfect'
    elif total < n:
        return 'Deficient'
    else:
        return 'Abundant'


N = int(input())
print(check_perfect(N))