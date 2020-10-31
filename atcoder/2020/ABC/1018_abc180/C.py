N = int(input())

def divisors(n):
    '''約数列挙'''
    div = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n//i)

    # divisors.sort()  # ソートの必要あれば
    return div


ans = sorted(divisors(N))
for i in ans:
    print(i)